from typing import Dict
from models import Item, SpecialOffer

class Checkout:

    def __init__(self):
        self.items: Dict[str, Item] = {
            'A': Item('A', 50, SpecialOffer(3, 130)),
            'B': Item('B', 30, SpecialOffer(2, 45)),
            'C': Item('C', 20),
            'D': Item('D', 15)
        }

    def _validate_input(self, skus: str)-> bool:
        pass

    def _count_items(self, skus: str)-> int:
        pass

    def _calculate_items_total(self, skus: str, quantity: int)-> int:
        pass

    def checkout(self, skus: str) -> int:
        if not skus:
            return 0
        if not self._validate_input(skus):
            return -1
        
        items_count = self._count_items(skus)
        total = sum(self._calculate_items_total(sku, count) for sku, count in items_count.items())
