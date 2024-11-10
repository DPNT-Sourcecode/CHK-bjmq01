from dataclasses import dataclass
from typing import Optional

@dataclass
class SpecialOffer:
    quantity: int
    special_price: int

@dataclass
class Item:
    sku: str
    price: int
    special_offer: Optional[SpecialOffer] = None
