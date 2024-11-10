import unittest
import checkout_solution


class TestCheckout(unittest.TestCase):
    """Testcase class for checkout"""

    def setup(self):
        pass


    def test_empty_basket(self):
        self.assertEqual(checkout_solution.checkout(""), 0)

    def test_invalid_inout(self):
        self.assertEqual(checkout_solution.checkout("X"), 0)
        self.assertEqual(checkout_solution.checkout("1"), 0)
        self.assertEqual(checkout_solution.checkout("-"), 0)

    def test_single_items(self):
        self.assertEqual(checkout_solution.checkout("A"), 50)
        self.assertEqual(checkout_solution.checkout("B"), 30)
        self.assertEqual(checkout_solution.checkout("C"), 20)
        self.assertEqual(checkout_solution.checkout("D"), 15)

    def test_multiple_items(self):
        self.assertEqual(checkout_solution.checkout("ABCD"), 115)
        self.assertEqual(checkout_solution.checkout("CC"), 40)

    def test_special_offers(self):
        self.assertEqual(checkout_solution.checkout("AAA"), 130)
        self.assertEqual(checkout_solution.checkout("BB"), 45)
        self.assertEqual(checkout_solution.checkout("AAAA"), 180)
        self.assertEqual(checkout_solution.checkout("AAAAA"), 230)
        self.assertEqual(checkout_solution.checkout("AAAAAA"), 260)    

    def test_combined_offers(self):
        self.assertEqual(checkout_solution.checkout("AAABB"), 175)
        self.assertEqual(checkout_solution.checkout("AAABBCD"), 210)


    def test_order_independence(self):
        self.assertEqual(checkout_solution.checkout("ABCD"), self.assertEqual(checkout_solution.checkout("DCBA"), 0))



        
if __name__ == '__main__':
    unittest.main()