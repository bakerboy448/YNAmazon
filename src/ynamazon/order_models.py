from amazonorders.entity.order import Order
from amazonorders.orders import AmazonOrders
from amazonorders.session import AmazonSession

from .base import ListRootModel


class AmazonOrderModels(ListRootModel[Order]):
    @classmethod
    def get_order_history(cls, session: "AmazonSession", years: list[int]):
        """Fetches order history and returns an AmazonOrderModels instance.

        Args:
            session (AmazonSession): An authenticated AmazonSession instance.
            years (list[int]): List of years to fetch orders for. Defaults to None, which fetches all available years.

        Returns:
            AmazonOrderModels: An instance containing the fetched orders.
        """
        amazon_orders = AmazonOrders(session)
        orders: list[Order] = []
        for year in years:
            year_orders = amazon_orders.get_order_history(year=year)
            orders.extend(year_orders)

        return cls.model_validate(orders)

    def sort_by_order_placed_date(self, reverse: bool = False) -> None:
        """Sorts the orders by order placed date.

        Args:
            reverse (bool, optional): Whether to sort in descending order. Defaults to False.
        """
        self.root.sort(key=lambda order: order.order_placed_date, reverse=reverse)
