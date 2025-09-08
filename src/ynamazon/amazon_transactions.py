# pyright: reportDeprecated=false
import os
import tempfile
from datetime import date
from decimal import Decimal
from typing import Annotated, Union, cast  # ,  Self  # not available python <3.11

from amazonorders.entity.order import Order
from amazonorders.entity.transaction import Transaction
from amazonorders.session import AmazonSession
from cache_decorator import Cache
from loguru import logger
from pydantic import AnyUrl, BaseModel, EmailStr, Field, SecretStr, field_validator
from rich import print as rprint
from rich.table import Table

from ynamazon.order_models import AmazonOrderModels
from ynamazon.transaction_models import AmazonTransactionModels

from .settings import settings
from .types_pydantic import AmazonItemType


class AmazonTransactionWithOrderInfo(BaseModel):
    """Amazon transaction with order info."""

    completed_date: date
    transaction_total: Annotated[
        Decimal, Field(description="Value is inverted, e.g. -10.00 -> 10.00")
    ]
    order_total: Decimal
    order_number: str
    order_link: AnyUrl
    items: list[AmazonItemType]

    @field_validator("transaction_total", mode="after")
    @classmethod
    def invert_value(cls, value: Decimal) -> Decimal:
        """Inverts the value."""
        return -value

    # TODO: when dropping support for python <3.11, use Self
    @classmethod
    def from_transaction_and_orders(cls, orders_dict: "dict[str, Order]", transaction: Transaction):
        """Creates an instance from an order and transactions."""
        order = orders_dict.get(transaction.order_number)
        if order is None:
            raise ValueError(f"Order with number {transaction.order_number} not found.")
        return cls(
            completed_date=transaction.completed_date,
            transaction_total=transaction.grand_total,  # pyright: ignore[reportArgumentType]
            order_total=order.grand_total,  # pyright: ignore[reportArgumentType]
            order_number=order.order_number,
            order_link=order.order_details_link,  # pyright: ignore[reportArgumentType]
            items=order.items,
        )


class AmazonConfig(BaseModel):
    """Configuration for Amazon transactions.

    Attributes:
        username (EmailStr): Amazon account email.
        password (SecretStr): Amazon account password.
    """

    username: EmailStr = Field(default_factory=lambda: settings.amazon_user)
    password: SecretStr = Field(default_factory=lambda: settings.amazon_password)
    debug: bool = False

    def amazon_session(self) -> AmazonSession:
        """Creates an Amazon session."""
        logger.debug(f"Creating Amazon session for with debug={self.debug}")
        return AmazonSession(
            username=self.username,
            password=self.password.get_secret_value(),
            debug=self.debug,
        )


def validate_year(year: str | int) -> int:
    """Validates that a year has been entered with 4 digits."""
    year_str = str(year)
    if len(year_str) == 4 and year_str.isdigit():
        return int(year_str)
    raise ValueError("Year must be a 4-digit number.")


class AmazonTransactionRetriever:
    def __init__(
        self,
        amazon_config: AmazonConfig,
        order_years: list[str | int] | None = None,
        transaction_days: int = 31,
        force_refresh_amazon: bool = False,
    ):
        """Initialize an AmazonTransactionRetriever.

        amazon_config (AmazonConfig): Configuration for Amazon, primarily credentials
        order_years (list[int] | None): A list of years to fetch transactions for. `None` for the current year.
        transaction_days (int): Number of days to fetch transactions for. Defaults to 31.
        force_refresh_amazon (bool): Refresh cache by fetching transactions directly from Amazon.
        """
        self.amazon_config: AmazonConfig = amazon_config
        self.order_years: list[int] = self.normalize_years(order_years)
        self.transaction_days: int = transaction_days
        self.force_refresh_amazon: bool = force_refresh_amazon

        # for memoizing the results of method calls
        self._session: AmazonSession | None = None
        self._amazon_orders: AmazonOrderModels | None = None
        self._amazon_transactions: AmazonTransactionModels | None = None

    def get_amazon_transactions(self) -> list[AmazonTransactionWithOrderInfo]:
        """Get Amazon transactions linked to orders.

        This method exists as a layer to force caching to work one level below with all relevant parameters considered

        Returns:
            list[TransactionWithOrderInfo]: A list of transactions with order info
        """
        return cast(
            "list[AmazonTransactionWithOrderInfo]",
            self._get_amazon_transactions(
                order_years=self.order_years,
                transaction_days=self.transaction_days,
                amazon_config=self.amazon_config,
                use_cache=not self.force_refresh_amazon,
            ),
        )

    # HACK: unused parameters are needed for caching to work correctly
    @Cache(
        validity_duration="2h",
        enable_cache_arg_name="use_cache",
        cache_path=os.path.join(
            tempfile.gettempdir(),
            "ynamazon",
            "amazon_transactions_get_amazon_transactions_{_hash}.pkl",
        ),
    )
    def _get_amazon_transactions(
        self,
        order_years: list[str],  # pyright: ignore[reportUnusedParameter]
        transaction_days: int,  # pyright: ignore[reportUnusedParameter]
        amazon_config: AmazonConfig,  # pyright: ignore[reportUnusedParameter]
        use_cache: bool = True,  # pyright: ignore[reportUnusedParameter]
    ) -> list[AmazonTransactionWithOrderInfo]:
        orders_dict = {order.order_number: order for order in self.fetch_amazon_orders()}

        amazon_transactions = self.fetch_amazon_transactions()

        amazon_transaction_with_order_details: list[AmazonTransactionWithOrderInfo] = []
        for transaction in amazon_transactions:
            try:
                amazon_transaction_with_order_details.append(
                    AmazonTransactionWithOrderInfo.from_transaction_and_orders(
                        orders_dict=orders_dict, transaction=transaction
                    )
                )
            except ValueError:
                logger.debug(
                    f"Transaction {transaction.order_number} not found in retrieved orders."
                )
                continue

        return amazon_transaction_with_order_details

    def fetch_amazon_orders(self) -> AmazonOrderModels:
        """Returns a list of Amazon orders.

        Args:
            years (Sequence[int] | None): A sequence of years to fetch orders for. `None` for the current year.

        Returns:
            list[Order]: A list of Amazon orders.
        """
        if self._amazon_orders is not None:
            return self._amazon_orders

        orders = AmazonOrderModels.get_order_history(self.get_session(), self.order_years)
        orders.sort_by_order_placed_date()

        self._amazon_orders = orders

        return self._amazon_orders

    def fetch_amazon_transactions(self) -> AmazonTransactionModels:
        """Fetches and sorts Amazon transactions."""
        if self._amazon_transactions is not None:
            return self._amazon_transactions

        transactions = AmazonTransactionModels.get_transactions(
            self.get_session(), self.transaction_days
        )
        transactions.sort_by_completed_date()

        self._amazon_transactions = transactions

        return self._amazon_transactions

    def get_session(self) -> AmazonSession:
        if self._session is not None:
            return self._session

        amazon_session = self.amazon_config.amazon_session()
        amazon_session.login()

        if amazon_session.is_authenticated:
            self._session = amazon_session
            return self._session
        raise ValueError("Failed to authenticate with Amazon.")

    @classmethod
    def normalize_years(cls, years: list[str | int] | None = None) -> list[int]:
        if years is None:
            return [date.today().year]

        return [validate_year(year) for year in years]


def print_amazon_transactions(
    amazon_transaction_with_order_details: list[AmazonTransactionWithOrderInfo],
):
    """Prints a list of transactions to the screen for inspection.

    Args:
        amazon_transaction_with_order_details (list[TransactionWithOrderInfo]): a list of transactions to print
    """
    rprint(f"found {len(amazon_transaction_with_order_details)} transactions")
    table = Table(title="Amazon Transactions")
    table.add_column("Completed Date", justify="center")
    table.add_column("Transaction Total", justify="right")
    table.add_column("Order Total", justify="right")
    table.add_column("Order Number", justify="center")
    table.add_column("Order Link", justify="center")
    table.add_column("Item Names", justify="left")

    for transaction in amazon_transaction_with_order_details:
        table.add_row(
            str(transaction.completed_date),
            f"${transaction.transaction_total:.2f}",
            f"${transaction.order_total:.2f}",
            transaction.order_number,
            str(transaction.order_link),
            " | ".join(_truncate_title(item.title) for item in transaction.items),
        )

    rprint(table)


def _truncate_title(title: str, max_length: int = 20) -> str:
    """Truncates the title to a maximum length."""
    if len(title) > max_length:
        return title[: max_length - 3] + "..."
    return title


def locate_amazon_transaction_by_amount(
    amazon_trans: list[AmazonTransactionWithOrderInfo], amount: Union[float, Decimal]
) -> Union[int, None]:
    """Given an amount, locate a matching Amazon transaction.

    Args:
        amazon_trans (list[TransactionWithOrderInfo]): A list of Amazon transactions
        amount (int): An amount to match

    Returns:
        int | None: Index of matched transaction in `amazon_trans` or None if no match
    """
    amount = Decimal(amount)
    for idx, a_tran in enumerate(amazon_trans):
        if a_tran.transaction_total == -amount:
            return idx

    return None


# if __name__ == "__main__":
# print_amazon_transactions(AmazonTransactionRetriever.new()
