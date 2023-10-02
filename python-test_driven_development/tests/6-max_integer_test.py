#!/usr/bin/python3
"""Unit tests for the max_integer([..]) function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_regular_case(self):
        result = max_integer([1, 3, 5, 2])
        self.assertEqual(result, 5)

    def test_all_negative(self):
        result = max_integer([-10, -3, -20, -5])
        self.assertEqual(result, -3)

    def test_empty_array(self):
        result = max_integer([])
        self.assertEqual(result, None)

    def test_single_value(self):
        result = max_integer([8])
        self.assertEqual(result, 8)

    def test_max_at_start(self):
        result = max_integer([9, 2, 3, 4])
        self.assertEqual(result, 9)

    def test_max_at_end(self):
        result = max_integer([1, 2, 3, 9])
        self.assertEqual(result, 9)

    def test_mixed_negative_and_positive(self):
        result = max_integer([-1, -5, 3, 2])
        self.assertEqual(result, 3)

    def test_float_and_int_mixed(self):
        result = max_integer([1.5, 2, 3.5, 4])
        self.assertEqual(result, 4)

    def test_str_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4])
