from amazonorders.entity.transaction import Transaction
from amazonorders.session import AmazonSession
from amazonorders.transactions import AmazonTransactions

from .base import ListRootModel


class AmazonTransactionModels(ListRootModel[Transaction]):
    @classmethod
    def get_transactions(cls, session: "AmazonSession", days: int):
        """Fetches transactions and returns an AmazonTransactionModels instance.

        Args:
            session (AmazonSession): An authenticated AmazonSession instance.
            days (int): Number of days back to fetch transactions for.

        Returns:
            AmazonTransactionModels: An instance containing the fetched transactions.
        """
        transactions = AmazonTransactions(session).get_transactions(days)

        return cls.model_validate(transactions)

    def sort_by_completed_date(self, reverse: bool = False) -> None:
        """Sorts the transactions by completed date.

        Args:
            reverse (bool, optional): Whether to sort in descending order. Defaults to False.
        """
        self.root.sort(key=lambda transaction: transaction.completed_date, reverse=reverse)
