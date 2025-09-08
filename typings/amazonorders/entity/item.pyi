from datetime import date

from amazonorders.conf import AmazonOrdersConfig
from amazonorders.entity.parsable import Parsable
from amazonorders.entity.seller import Seller
from bs4 import Tag

class Item(Parsable):
    title: str
    link: str
    price: float | None
    seller: Seller | None
    condition: str | None
    return_eligible_date: date | None
    image_link: str | None
    quantity: int | None

    def __init__(self, parsed: Tag, config: AmazonOrdersConfig) -> None: ...
    def __lt__(self, other: Item) -> bool: ...
