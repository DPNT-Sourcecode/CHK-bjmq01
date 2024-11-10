import unittest
import hello_solution

class TestHelloClass(unittest.TestCase):
    """Testing the hello world program
    
    --ignoring since this is trial
    """


    def test_hello(self):
        # basic functionality being tested
        self.assertEqual(hello_solution.hello(""), "Hello World")