import time
from collections.abc import Callable, Generator, Iterable
from contextlib import contextmanager
from datetime import date, timedelta
from decimal import Decimal
from functools import wraps
from typing import Any, ParamSpec, TypeVar

from loguru import logger
from pydantic import AnyUrl
from rich import print as rprint
from rich.table import Table
from ynab.api.payees_api import PayeesApi
from ynab.api.transactions_api import TransactionsApi
from ynab.api_client import ApiClient
from ynab.configuration import Configuration
from ynab.exceptions import ApiException, UnauthorizedException
from ynab.models.existing_transaction import ExistingTransaction
from ynab.models.hybrid_transaction import HybridTransaction
from ynab.models.payee import Payee
from ynab.models.put_transaction_wrapper import PutTransactionWrapper

from ynamazon import USER_AGENT
from ynamazon.base import ListRootModel
from ynamazon.exceptions import YnabSetupError
from ynamazon.settings import settings

YNAB_MEMO_LIMIT = 500
_RATE_LIMIT_DELAYS = (60, 120, 240)  # seconds between retries on 429

_P = ParamSpec("_P")
_R = TypeVar("_R")

default_configuration = Configuration(access_token=settings.ynab_api_key.get_secret_value())
my_budget_id = settings.ynab_budget_id


def ynab_rate_limit_retry(func: Callable[_P, _R]) -> Callable[_P, _R]:
    """Retry YNAB API calls on 429 rate limit with exponential backoff."""

    @wraps(func)
    def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _R:
        for attempt, delay in enumerate(_RATE_LIMIT_DELAYS):
            try:
                return func(*args, **kwargs)
            except UnauthorizedException as exc:
                logger.error(f"YNAB authentication failed: {exc}")
                raise
            except ApiException as exc:
                if exc.status != 429:
                    _log_ynab_api_error(exc)
                    raise
                logger.warning(
                    f"YNAB rate limit hit (attempt {attempt + 1}/{len(_RATE_LIMIT_DELAYS)}). "
                    f"Retrying in {delay}s..."
                )
                time.sleep(delay)
        # Final attempt — let exceptions propagate
        return func(*args, **kwargs)

    return wrapper


def _log_ynab_api_error(exc: ApiException) -> None:
    """Log a YNAB API error with meaningful context."""
    status = exc.status or "unknown"
    reason = exc.reason or "no reason"
    logger.error(f"YNAB API error ({status}): {reason}")
    if exc.body:
        logger.debug(f"YNAB API response body: {exc.body}")


@contextmanager
def ynab_api_client(configuration: Configuration) -> Generator[ApiClient, None, None]:
    """Create an ApiClient with the YNAmazon User-Agent set."""
    with ApiClient(configuration=configuration) as api_client:
        api_client.user_agent = USER_AGENT
        yield api_client


class TempYnabTransaction(HybridTransaction):
    """Temporary YNAB transaction."""

    @property
    def amount_decimal(self) -> Decimal:
        """Returns the amount in currency."""
        return self.amount / Decimal("1000")


def translate_hybrid_to_temp(
    transactions: list["HybridTransaction"],
) -> list[TempYnabTransaction]:
    """Converts a list of YNAB transactions to temporary YNAB transactions.

    Args:
        transactions (list[HybridTransaction]): The list of YNAB transactions.

    Returns:
        list[TempYnabTransaction]: The list of temporary YNAB transactions.
    """
    return [
        TempYnabTransaction.model_validate(transaction.model_dump()) for transaction in transactions
    ]


class TempYnabTransactions(ListRootModel[TempYnabTransaction]):
    @classmethod
    def from_hybrid(cls, transactions: list[HybridTransaction]) -> "TempYnabTransactions":
        temp_transactions = translate_hybrid_to_temp(transactions)
        return cls(root=temp_transactions)

    @classmethod
    def get_by_payee(
        cls, payee: Payee, *, configuration: Configuration, budget_id: str
    ) -> "TempYnabTransactions":
        return cls.from_hybrid(_fetch_transactions_by_payee(configuration, budget_id, payee.id))


# Module-level payee cache: keyed by (access_token, budget_id)
_payee_cache: dict[tuple[str, str], "Payees"] = {}


class Payees(ListRootModel[Payee]):
    @classmethod
    def get_by_budget(
        cls,
        *,
        configuration: Configuration,
        budget_id: str,
        use_cache: bool = True,
    ) -> "Payees":
        cache_key = (configuration.access_token or "", budget_id)
        if use_cache and cache_key in _payee_cache:
            logger.debug("Using cached payee list")
            return _payee_cache[cache_key]

        result = cls.model_validate(_fetch_payees(configuration, budget_id))
        _payee_cache[cache_key] = result
        return result

    def get_named_payee(self, name: str) -> Payee | None:
        for payee in self.root:
            if payee.name == name:
                return payee
        return None


@ynab_rate_limit_retry
def _fetch_payees(configuration: Configuration, budget_id: str) -> list[Payee]:
    """Fetch payees from YNAB API with rate limit retry."""
    with ynab_api_client(configuration) as api_client:
        response = PayeesApi(api_client).get_payees(budget_id=budget_id)
    return response.data.payees


@ynab_rate_limit_retry
def _fetch_transactions_by_payee(
    configuration: Configuration, budget_id: str, payee_id: str
) -> list[HybridTransaction]:
    """Fetch transactions by payee from YNAB API with rate limit retry."""
    with ynab_api_client(configuration) as api_client:
        response = TransactionsApi(api_client).get_transactions_by_payee(
            budget_id=budget_id,
            payee_id=payee_id,
        )
    return response.data.transactions


@ynab_rate_limit_retry
def _update_transaction_api(
    configuration: Configuration,
    budget_id: str,
    transaction_id: str,
    data: PutTransactionWrapper,
) -> None:
    """Update a YNAB transaction with rate limit retry."""
    with ynab_api_client(configuration) as api_client:
        TransactionsApi(api_client=api_client).update_transaction(
            budget_id=budget_id, transaction_id=transaction_id, data=data
        )


def get_payees_by_budget(
    configuration: Configuration | None = None,
    budget_id: str | None = None,
) -> list["Payee"]:
    """Returns a list of payees by budget ID.

    Args:
        configuration (Configuration | None): The YNAB API configuration.
        budget_id (str | None): The budget ID.

    Returns:
        list[Payee]: A list of payees.
    """
    configuration = configuration or default_configuration
    budget_id = budget_id or my_budget_id.get_secret_value()
    return _fetch_payees(configuration, budget_id)


def get_transactions_by_payee(
    payee: Payee,
    configuration: Configuration | None = None,
    budget_id: str | None = None,
) -> list[TempYnabTransaction]:
    """Returns a list of transactions by payee.

    Args:
        payee (Payee): The payee object.
        configuration (Configuration | None): The YNAB API configuration.
        budget_id (str | None): The budget ID.

    Returns:
        list[TempYnabTransaction]: A list of transactions.
    """
    configuration = configuration or default_configuration
    budget_id = budget_id or my_budget_id.get_secret_value()
    return translate_hybrid_to_temp(
        _fetch_transactions_by_payee(configuration, budget_id, payee.id)
    )


def get_ynab_transactions(
    configuration: Configuration | None = None,
    budget_id: str | None = None,
    force: bool = False,
    days: int = 31,
) -> tuple[TempYnabTransactions, "Payee"]:
    """Returns a tuple of YNAB transactions and the payee.

    Args:
        configuration (Configuration | None): The YNAB API configuration.
        budget_id (str | None): The budget ID.
        force (bool): If True, include transactions with existing memos.
        days (int): Number of days to look back for transactions.

    Returns:
        tuple[list[HybridTransaction], Payee] | None: A tuple of YNAB transactions and the payee.

    Raises:
        YnabSetupError: If the payees are not found in YNAB.
    """
    configuration = configuration or default_configuration
    budget_id = budget_id or my_budget_id.get_secret_value()

    payees = Payees.get_by_budget(configuration=configuration, budget_id=budget_id)

    rprint("Finding payees...")
    amazon_with_memo_payee = payees.get_named_payee(settings.ynab_payee_name_processing_completed)
    if amazon_with_memo_payee is None:
        raise YnabSetupError(
            f"Payee '{settings.ynab_payee_name_processing_completed}' not found in YNAB."
        )

    min_date = date.today() - timedelta(days=days)

    if settings.match_empty_memo or force:
        # Match transactions by "Amazon" payee
        ynab_transactions = TempYnabTransactions.get_by_payee(
            amazon_with_memo_payee, configuration=configuration, budget_id=budget_id
        )
        if force:
            # Force mode: match all Amazon transactions within date range
            ynab_transactions.filter(lambda t: t.var_date >= min_date)
        else:
            # Normal mode: empty memo within date range, filtered by approved status setting
            def matches_filter(t: TempYnabTransaction) -> bool:
                if t.memo or t.var_date < min_date:
                    return False
                # Check if transaction's approved status matches allowed statuses
                status = "approved" if t.approved else "unapproved"
                return status in settings.ynab_approved_statuses

            ynab_transactions.filter(matches_filter)
    else:
        # Original behavior: require "Amazon - Needs Memo" payee
        amazon_needs_memo_payee = payees.get_named_payee(settings.ynab_payee_name_to_be_processed)
        if amazon_needs_memo_payee is None:
            raise YnabSetupError(
                f"Payee '{settings.ynab_payee_name_to_be_processed}' not found in YNAB."
            )
        ynab_transactions = TempYnabTransactions.get_by_payee(
            amazon_needs_memo_payee, configuration=configuration, budget_id=budget_id
        )
        ynab_transactions.filter(lambda t: not t.approved and t.var_date >= min_date)

    return ynab_transactions, amazon_with_memo_payee


def update_ynab_transaction(
    transaction: "HybridTransaction",
    memo: str,
    payee_id: str,
    configuration: Configuration | None = None,
    budget_id: str | None = None,
) -> None:
    """Updates a YNAB transaction with the given memo and payee ID.

    Args:
        transaction (HybridTransaction): The transaction to update.
        memo (str): The memo to set.
        payee_id (str): The payee ID to set.
        configuration (Configuration | None): The YNAB API configuration.
        budget_id (str | None): The budget ID.
    """
    configuration = configuration or default_configuration
    budget_id = budget_id or my_budget_id.get_secret_value()
    data = PutTransactionWrapper(
        transaction=ExistingTransaction.model_validate(transaction.to_dict())
    )

    # Convert memo to string if it's a MultiLineText object
    memo_str = str(memo)

    # Ensure memo doesn't exceed character limit
    if len(memo_str) > YNAB_MEMO_LIMIT:
        logger.warning(
            f"Memo exceeds {YNAB_MEMO_LIMIT} character limit ({len(memo_str)} chars). Truncating..."
        )
        # Keep the important parts - first warning line, and the URL at the end
        lines = memo_str.split("\n")

        # Extract the URL at the end (it must be preserved)
        url_line = lines[-1]

        # Keep the warning header if it exists
        header = ""
        if len(lines) > 0 and "-This transaction doesn" in lines[0]:
            header = lines[0] + "\n\n"

        # Calculate remaining space for content
        remaining_space = YNAB_MEMO_LIMIT - len(header) - len(url_line) - 4  # 4 chars for "...\n"

        # Get middle content (item list) and truncate if needed
        middle_content = "\n".join(lines[1:-1])
        if len(middle_content) > remaining_space:
            middle_content = middle_content[:remaining_space] + "..."

        # Combine the parts to stay under limit
        memo_str = f"{header}{middle_content}\n{url_line}"

    logger.debug(f"Updating YNAB transaction {transaction.id} with memo length {len(memo_str)}")
    data.transaction.memo = memo_str
    data.transaction.payee_id = payee_id
    _update_transaction_api(configuration, budget_id, transaction.id, data)
    logger.info(f"Successfully updated transaction {transaction.id}")


_T = TypeVar("_T", bound=Payee)


def find_item_by_attribute(items: Iterable[_T], attribute: str, value: Any) -> _T | None:
    """Finds an item in a list by its attribute value.

    Args:
        items (Iterable[_T]): The list of items to search.
        attribute (str): The attribute name to search for.
        value (Any): The value to match.

    Returns:
        _T | None: The found item or None if not found.
    """
    item_list = [item for item in items if getattr(item, attribute) == value]
    if not item_list:
        return None
    if len(item_list) > 1:
        logger.warning(f"Multiple items found with {attribute} = {value}. Returning the first one.")

    return item_list[0]


def print_ynab_transactions(transactions: list[TempYnabTransaction]) -> None:
    """Prints YNAB transactions in a table format.

    Args:
        transactions (list[HybridTransaction]): The list of transactions to print.
    """
    rprint(f"found {len(transactions)} transactions")
    table = Table(title="YNAB Transactions")
    table.add_column("Date", justify="left", style="cyan", no_wrap=True)
    table.add_column("Amount", justify="right", style="green")

    for transaction in transactions:
        table.add_row(str(transaction.var_date), f"${-transaction.amount_decimal:.2f}")

    rprint(table)


def markdown_formatted_title(title: str, url: str | AnyUrl) -> str:
    """Returns a formatted item title in markdown or raw format, dependent on ynab_use_markdown.

    Args:
        title (str): The name for the item
        url (str): The URL to link to

    Returns:
        str: A URL string suitable for injection into the memo
    """
    if settings.ynab_use_markdown:
        return f"[{title}]({url})"

    return title


def markdown_formatted_link(title: str, url: str | AnyUrl) -> str:
    """Returns a link in markdown or raw format, dependent on ynab_use_markdown.

    Args:
        title (str): The name for the link
        url (str): The URL to link to

    Returns:
        str: A URL string suitable for injection into the memo
    """
    if settings.ynab_use_markdown:
        return f"[{title}]({url})"

    if isinstance(url, AnyUrl):
        url = str(url)

    return url


if __name__ == "__main__":
    ynab_transactions, _ = get_ynab_transactions()
    if not ynab_transactions:
        rprint("[bold red]No transactions found.[/]")
        exit(1)
    print_ynab_transactions(transactions=ynab_transactions)  # pyright: ignore[reportArgumentType]
