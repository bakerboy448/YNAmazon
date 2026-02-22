from dataclasses import dataclass, field
from difflib import unified_diff
from typing import TYPE_CHECKING

from loguru import logger
from rich.console import Console
from rich.prompt import Confirm
from rich.syntax import Syntax

from ynamazon.amazon_transactions import (
    AmazonConfig,
    AmazonTransactionRetriever,
    locate_amazon_transaction_by_amount,
)
from ynamazon.exceptions import YnabSetupError
from ynamazon.settings import settings
from ynamazon.ynab_transactions import default_configuration as ynab_configuration
from ynamazon.ynab_transactions import (
    get_ynab_transactions,
    update_ynab_transaction,
)

try:
    from ynamazon.ynab_memo import process_memo
except ImportError:
    pass

if TYPE_CHECKING:
    from ynab.configuration import Configuration


@dataclass
class SyncResult:
    """Summary of a sync run."""

    ynab_count: int = 0
    amazon_count: int = 0
    matched: int = 0
    skipped: int = 0
    updated: int = 0
    errors: list[str] = field(default_factory=list)


# TODO: reduce complexity of this function
def process_transactions(  # noqa: C901
    amazon_config: AmazonConfig | None = None,
    ynab_config: "Configuration | None" = None,
    budget_id: str | None = None,
    force_refresh_amazon: bool = False,
    dry_run: bool = False,
    force: bool = False,
    non_interactive: bool | None = None,
) -> SyncResult:
    """Match YNAB transactions to Amazon Transactions and optionally update YNAB Memos."""
    amazon_config = amazon_config or AmazonConfig()
    ynab_config = ynab_config or ynab_configuration
    budget_id = budget_id or settings.ynab_budget_id.get_secret_value()
    # Use passed value or fall back to settings
    non_interactive = non_interactive if non_interactive is not None else settings.non_interactive

    result = SyncResult()
    console = Console()

    if dry_run:
        console.print("[bold yellow]DRY RUN MODE - No changes will be made[/]")

    # Get transaction days from amazon config
    days = amazon_config.transaction_days if amazon_config else 31

    try:
        ynab_trans, amazon_with_memo_payee = get_ynab_transactions(
            configuration=ynab_config, budget_id=budget_id, force=force, days=days
        )
    except YnabSetupError:
        console.print("[bold red]No matching Transactions found in YNAB. Exiting.[/]")
        return result

    console.print("[cyan]Starting search for Amazon transactions...[/]")
    amazon_trans = AmazonTransactionRetriever(
        amazon_config=amazon_config, force_refresh_amazon=force_refresh_amazon
    ).get_amazon_transactions()

    console.print(f"[green]{len(amazon_trans)} Amazon transactions retrieved successfully.[/]")
    result.ynab_count = len(ynab_trans)
    result.amazon_count = len(amazon_trans)

    console.print("[cyan]Starting to look for matching transactions...[/]")
    for ynab_tran in ynab_trans:
        console.print(
            f"[cyan]Looking for an Amazon Transaction that matches this YNAB transaction:[/] {ynab_tran.var_date} ${ynab_tran.amount / -1000:.2f}"
        )
        # because YNAB uses "milliunits" for amounts, we need to convert to dollars
        logger.debug(f"YNAB transaction amount [dollars]: {ynab_tran.amount_decimal}")
        amazon_tran_index = locate_amazon_transaction_by_amount(
            amazon_trans=amazon_trans, amount=ynab_tran.amount_decimal
        )
        if not amazon_tran_index:
            console.print("[bold yellow]**** Could not find a matching Amazon Transaction![/]")
            result.skipped += 1
            continue

        amazon_tran = amazon_trans[amazon_tran_index]
        result.matched += 1
        console.print(
            f"[green]Matching Amazon Transaction:[/] {amazon_tran.completed_date} ${amazon_tran.transaction_total:.2f}"
        )

        # Build memo: "Item A ($XX.XX), Item B ($XX.XX) | Order #XXX"
        def format_item(item) -> str:
            price_str = f"(${item.price:.2f})" if item.price else ""
            return f"{item.title} {price_str}".strip()

        items_str = ", ".join(format_item(item) for item in amazon_tran.items)
        memo_text = f"{items_str} | Order #{amazon_tran.order_number}"

        # Add warning if partial order
        if amazon_tran.transaction_total != amazon_tran.order_total:
            memo_text = f"[Partial - order total ${amazon_tran.order_total:.2f}] {memo_text}"

        console.print("[bold u green]Memo:[/]")
        console.print(memo_text)

        # Only use the AI processing if OpenAI is installed
        if "process_memo" in globals():
            memo_text = process_memo(memo_text)  # pyright: ignore[reportPossiblyUnboundVariable]

        # Check if dates match within tolerance
        date_diff = abs((amazon_tran.completed_date - ynab_tran.var_date).days)
        dates_within_tolerance = date_diff <= settings.date_mismatch_tolerance_days

        if amazon_tran.completed_date != ynab_tran.var_date:
            console.print(
                f"[yellow]**** The dates don't match! YNAB: {ynab_tran.var_date} Amazon: {amazon_tran.completed_date} (diff: {date_diff} days)[/]"
            )
            if dates_within_tolerance:
                console.print(
                    f"[green]Within tolerance ({settings.date_mismatch_tolerance_days} days) - auto-accepting[/]"
                )
                continue_match = True
            elif settings.auto_accept_date_mismatch or non_interactive:
                console.print("[yellow]Auto-accepting date mismatch (non-interactive mode)[/]")
                continue_match = True
            else:
                continue_match = Confirm.ask(
                    "[bold red]Continue matching this transaction anyway?[/]",
                    console=console,
                )
            if not continue_match:
                console.print("[yellow]Skipping this transaction...[/]")
                result.skipped += 1
                continue
            else:
                _ = amazon_trans.pop(amazon_tran_index)
                console.log("Removing matched transaction from search")

        if dry_run:
            console.print("[bold yellow]DRY RUN: Would update this transaction[/]")
            current = ynab_tran.memo or ""
            if current != memo_text:
                diff = unified_diff(
                    current.splitlines(keepends=True),
                    memo_text.splitlines(keepends=True),
                    fromfile="current",
                    tofile="proposed",
                )
                diff_text = "".join(diff)
                if diff_text:
                    console.print(Syntax(diff_text, "diff", theme="monokai"))
                else:
                    console.print("[dim]No changes[/]")
            else:
                console.print("[dim]No changes needed[/]")
            console.print()
            result.skipped += 1
            continue

        if non_interactive:
            update_transaction = True
        else:
            update_transaction = Confirm.ask(
                "[bold cyan]Update YNAB transaction memo?[/]", console=console
            )
        if not update_transaction:
            console.print("[yellow]Skipping YNAB transaction update...[/]\n\n")
            console.print("[cyan i]Memo Preview[/]:")
            console.print(memo_text)
            result.skipped += 1
            continue

        console.print("[green]Updating YNAB transaction memo...[/]")

        update_ynab_transaction(
            transaction=ynab_tran,
            memo=memo_text,
            payee_id=amazon_with_memo_payee.id,
        )
        result.updated += 1
        console.print("\n\n")

    return result


if __name__ == "__main__":
    process_transactions()
