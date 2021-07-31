"""
This file demonstrates common uses for the Python unittest module
https://docs.python.org/3/library/unittest.html
"""
import random
import unittest
from main import fooBarQix


class TestSequenceFunctions(unittest.TestCase):
    """ This is one of potentially many TestCases """

    def setUp(self):
        self.seq = list(range(10))

    def test_zero(self):
        self.assertEqual(0, fooBarQix(0))

    def test_divisible_by_three(self):
        self.assertEqual("Foo", fooBarQix(6))

    def test_divisible_by_five(self):
        self.assertEqual("Bar", fooBarQix(10))
    
    def test_divisible_by_three_and_five(self):
        self.assertEqual("FooBar", fooBarQix(60))

    def test_divisible_by_seven(self):
        self.assertEqual("Qix", fooBarQix(14))

    def test_divisible_by_three_and_seven(self):
        self.assertEqual("FooQix", fooBarQix(21))

    def test_divisible_by_five_and_seven(self):
        self.assertEqual("BarQix", fooBarQix(140))

    def test_divisible_by_three_five_and_seven(self):
        self.assertEqual("FooBarQix", fooBarQix(210))

if __name__ == '__main__':
    unittest.main()
