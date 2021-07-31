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

if __name__ == '__main__':
    unittest.main()
