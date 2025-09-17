#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_start(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_max_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_negative_exists(self):
        self.assertLessEqual(max_integer([-1, -2, -3]), 0)

    def test_only_one(self):
        self.assertEqual(max_integer([100]), 100)

if __name__ == '__main__':
    unittest.main()
