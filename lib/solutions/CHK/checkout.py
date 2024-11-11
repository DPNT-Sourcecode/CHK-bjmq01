from typing import Dict
from .models import Item, SpecialOffer

class Checkout:

    def __init__(self):
        self.items: Dict[str, Item] = {
            'A': Item('A', 50, [SpecialOffer(5, 200), SpecialOffer(3, 130)]),
            'B': Item('B', 30, [SpecialOffer(2, 45),]),
            'C': Item('C', 20),
            'D': Item('D', 15),
            'E': Item('E', 40, [SpecialOffer(2, 80, 'B'),]),
            'F': Item('F', 10, [SpecialOffer(2, 80, 'F', 2),])
        }

    def _validate_input(self, skus: str)-> bool:
        return all(sku in self.items for sku in skus)

    def _count_items(self, skus: str)-> Dict[str, int]:
        return {sku: skus.count(sku) for sku in set(skus)}
    
    def _calculate_free_items(self, item_counts: Dict[str, int])-> Dict[str, int]:
        free_items = {}
        for sku, count in item_counts.items():
            item = self.items[sku]

            for offer in item.special_offers or []:
                if offer.free_item:
                    if offer.enforced_free_item_count==0 or count > offer.enforced_free_item_count:
                        free_count = count // offer.quantity
                        if offer.free_item in free_items:
                            free_items[offer.free_item] = max(free_items[offer.free_item], free_count)
                        else:
                            free_items[offer.free_item] = free_count
        return free_items
        

    def _calculate_item_total(self, sku: str, quantity: int)-> int:
        item = self.items[sku]
        if not item.special_offers:
            return quantity* item.price
        dp = [i * item.price for i in range(quantity + 1)]
        dp[0] = 0

        for qty in range(1, quantity + 1):
            for offer in item.special_offers:
                if not offer.free_item and qty >= offer.quantity:
                    dp[qty] = min(
                        dp[qty],
                        dp[qty-offer.quantity] + offer.special_price
                    )
        return dp[quantity]

        # for offer in item.special_offers:
        #     if not offer.free_item:
        #         special_deals = quantity // offer.quantity
        #         remaining_items = quantity % offer.quantity
        #         current_price = (special_deals * offer.special_price) + (remaining_items * item.price)
        #         best_price = min(best_price, current_price)

        # return best_price

    def checkout(self, skus: str) -> int:
        if not skus:
            return 0
        if not self._validate_input(skus=skus):
            return -1
        items_count = self._count_items(skus=skus)

        free_items = self._calculate_free_items(item_counts=items_count)
        print(free_items)
        print(items_count)

        for sku, free_count in free_items.items():
            if sku in items_count:
                items_count[sku] = max(0, items_count[sku] - free_count)
        
        print("after", items_count)
        total = sum(self._calculate_item_total(sku, count) for sku, count in items_count.items())
        print("total", total)
        return total







