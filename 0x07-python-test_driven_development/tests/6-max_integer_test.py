#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTestCase(unittest.TestCase):

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result, "Expected None for an empty list")

    def test_positive_numbers(self):
        result = max_integer([5, 10, 3, 8])
        self.assertEqual(result, 10, "Expected 10 as the maximum number")

    def test_negative_numbers(self):
        result = max_integer([-2, -8, -1, -5])
        self.assertEqual(result, -1, "Expected -1 as the maximum number")

    def test_mixed_numbers(self):
        result = max_integer([-10, 0, 15, -5, 7])
        self.assertEqual(result, 15, "Expected 15 as the maximum number")

    def test_single_element_list(self):
        result = max_integer([100])
        self.assertEqual(result, 100, "Expected 100 as the maximum number")

    def test_duplicate_numbers(self):
        result = max_integer([4, 2, 4, 2, 4])
        self.assertEqual(result, 4, "Expected 4 as the maximum number")

    def test_large_numbers(self):
        result = max_integer([1000000, 999999, 10000000, 888888])
        self.assertEqual(result, 10000000, "Expected 10000000 as the maximum number")
