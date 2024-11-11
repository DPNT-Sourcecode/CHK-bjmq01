

# noinspection PyUnusedLocal
# skus = unicode string
from checkout import Checkout

def checkout(skus: str)-> int:
    checkout_obj = Checkout()
    return checkout_obj.checkout(skus=skus)


if __name__ == '__main__':
    checkout("STX")
    print("expected: 45")
    checkout("STXSTX")
    print("expected: 90")
    checkout("SSS")
    print("expected: 45")
    # checkout("EEB")
    # checkout("AAAAAAAA")
    # checkout("NNNM")
    # c

