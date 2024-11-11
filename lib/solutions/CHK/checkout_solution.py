

# noinspection PyUnusedLocal
# skus = unicode string
from checkout import Checkout

def checkout(skus: str)-> int:
    checkout_obj = Checkout()
    return checkout_obj.checkout(skus=skus)


# if __name__ == '__main__':

    # checkout("EEB")
    # checkout("AAAAAAAA")

