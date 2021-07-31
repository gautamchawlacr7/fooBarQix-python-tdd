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
        self.assertEqual("*", fooBarQix(0))
    
    def test_other_numbers(self):
        self.assertEqual("1", fooBarQix(1))

    def test_divisible_by_three(self):
        self.assertEqual("FooFoo", fooBarQix(3))

    def test_divisible_by_five(self):
        self.assertEqual("BarBar", fooBarQix(5))
    
    def test_divisible_by_three_and_five(self):
        self.assertEqual("FooBarBar", fooBarQix(15))

    def test_divisible_by_seven(self):
        self.assertEqual("QixQix", fooBarQix(7))

    def test_divisible_by_three_and_seven(self):
        self.assertEqual("FooQix", fooBarQix(21))

    def test_divisible_by_five_and_seven(self):
        self.assertEqual("BarQix*", fooBarQix(140))

    def test_divisible_by_five_and_seven_with_three_five_inside(self):
        self.assertEqual("BarQixFooBar", fooBarQix(35))

    def test_divisible_by_three_five_and_seven(self):
        self.assertEqual("FooBarQix*", fooBarQix(210))

    #step 2 tests (keep track of zeroes by replacing with * and accomodate other numbers also)
    def test_one_step_two(self):
        self.assertEqual("1*1", fooBarQix(101))

    def test_two_step_two(self):
        self.assertEqual("FooFoo*Foo", fooBarQix(303))

    def test_three_step_two(self):
        self.assertEqual("FooBarQix*Bar", fooBarQix(105))

    def test_four_step_two(self):
        self.assertEqual("FooQix**", fooBarQix(10101))

if __name__ == '__main__':
    unittest.main()
