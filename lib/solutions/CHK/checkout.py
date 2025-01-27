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
            'F': Item('F', 10, [SpecialOffer(2, 80, 'F', 2),]),
            'G': Item('G', 20),
            'H': Item('H', 10, [SpecialOffer(5, 45), SpecialOffer(10, 80)]),
            'I': Item('I', 35),
            'J': Item('J', 60),
            'K': Item('K', 70, [SpecialOffer(2, 120),]),
            'L': Item('L', 90),
            'M': Item('M', 15),
            'N': Item('N', 40, [SpecialOffer(3, 120, 'M'),]),
            'O': Item('O', 10),
            'P': Item('P', 50, [SpecialOffer(5, 200),]),
            'Q': Item('Q', 30, [SpecialOffer(3, 80),]),
            'R': Item('R', 50, [SpecialOffer(3, 150, 'Q'),]),
            'S': Item('S', 20),
            'T': Item('T', 20),
            'U': Item('U', 40, [SpecialOffer(3, 120, 'U', 3),]),
            'V': Item('V', 50, [SpecialOffer(2, 90), SpecialOffer(3, 130),]),
            'W': Item('W', 20),
            'X': Item('X', 17),
            'Y': Item('Y', 20),
            'Z': Item('z', 21),

        }
        self.offer_group = {
            "total_count": 3,
            "group": "STXYZ"
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
                        if offer.enforced_free_item_count:
                            free_count = count // (offer.enforced_free_item_count + 1)
                        else:
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

        total = 0

        for sku, free_count in free_items.items():
            if sku in items_count:
                items_count[sku] = max(0, items_count[sku] - free_count)
        
        print("after", items_count)
        group_items = [
        (sku, count, self.items[sku].price)
        for sku, count in items_count.items()
        if sku in self.offer_group['group']
        ]
        
        group_items.sort(key=lambda x: x[2], reverse=True)
        
        total_group_offer_count = sum(count for _, count, _ in group_items)
        complete_groups = total_group_offer_count // 3
        remaining_items = total_group_offer_count % 3
        
        total = complete_groups * 45
        
        for sku in items_count:
            if sku in self.offer_group['group']:
                items_count[sku] = 0
        
        remaining_to_distribute = remaining_items
        for sku, original_count, _ in reversed(group_items):
            if remaining_to_distribute > 0:
                items_to_assign = min(remaining_to_distribute, original_count)
                items_count[sku] = items_to_assign
                remaining_to_distribute -= items_to_assign
        

        total += sum(self._calculate_item_total(sku, count) for sku, count in items_count.items())
        print("total", total)
        return total


