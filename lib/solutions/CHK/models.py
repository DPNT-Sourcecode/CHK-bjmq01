from dataclasses import dataclass
from typing import Optional, List

@dataclass
class SpecialOffer:
    quantity: int
    special_price: int = 0 # mean free item offer
    free_item: Optional[str] = None
    free_quantity: int = 1

@dataclass
class Item:
    sku: str
    price: int
    special_offers: List[SpecialOffer] = None

    def __post__init__(self):
        if self.special_offers is None:
            self.special_offers = []
