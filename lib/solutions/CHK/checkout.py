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
        return all(sku in self.items for sku in skus)

    def _count_items(self, skus: str)-> Dict[str, int]:
        return {sku: skus.count(sku) for sku in set(skus)}
        

    def _calculate_items_total(self, sku: str, quantity: int)-> int:
        item = self.items[sku]
        if not item.special_offer:
            return quantity* item.price
        special_offer = item.special_offer
        special_deals = quantity // special_offer.quantity
        remaining_items = quantity % special_offer.quantity
        return (special_deals * special_offer.special_price) + (remaining_items * item.price)

    def checkout(self, skus: str) -> int:
        if not skus:
            return 0
        if not self._validate_input(skus):
            return -1
        
        items_count = self._count_items(skus)
        total = sum(self._calculate_items_total(sku, count) for sku, count in items_count.items())

