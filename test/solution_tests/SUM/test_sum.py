from solutions.SUM import sum_solution
import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
        assert sum_solution.compute(0, 0) == 0
        assert sum_solution.compute(100, 100) == 200

    def test_type_mismatch(self):
         """Check for type mismatch"""

         invalid_inputs = [
             (1.5, 2),
             (1, "2"),
             (None, 5),
             ([], 1)
         ]
         for param1, param2 in invalid_inputs:
             with self.subTest(param1=param1, param2=param2):
                 with self.assertRaises(ValueError):
                     sum_solution.compute(param1, param2)





if __name__ == '__main__':
    unittest.main()