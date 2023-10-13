#!/usr/bin/python3
"""Unit tests for Square subclass"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_inheritance_from_base(self):
        self.assertTrue(issubclass(Square, Base))

    def test_inheritance_from_rectangle(self):
        self.assertTrue(issubclass(Square, Rectangle))

    def test_id_assignment_from_base(self):
        sqr = Square(6, 6, 7, 1)
        self.assertEqual(sqr.id, 1)

    def test_size_getter_and_setter(self):
        sqr = Square(8, 7, 6)
        self.assertEqual(sqr.size, 8)
        sqr.size = 3
        self.assertEqual(sqr.size, 3)

    def test_size_changes_width_and_height(self):
        sqr = Square(1, 2, 3)
        sqr.size = 4
        self.assertEqual(sqr.width, 4)
        self.assertEqual(sqr.height, 4)

    def test_square_update(self):
        sqr = Square(1, 2, 3, 4)
        sqr.update(5, 6, 7, 8)
        self.assertEqual(sqr.__str__(), "[Square] (5) 7/8 - 6")

    def test_square_update_from_dict(self):
        sqr = Square(4, 2, 2, 1)
        sqr.update(size=6, id=7, y=8)
        self.assertEqual(sqr.__str__(), "[Square] (7) 2/8 - 6")

    def test_square_to_dictionary(self):
        sqr = Square(6, 3, 3, 1)
        expected = {'id': 1, 'x': 3, 'size': 6, 'y': 3}
        self.assertEqual(sqr.to_dictionary(), expected)

    def test_type_errors_for_properties(self):
        with self.assertRaises(TypeError) as cm:
            sqr = Square("Bob", 2, 3)
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(TypeError) as cm:
            sqr = Square(1, "Bob", 5)
        self.assertEqual(str(cm.exception), "x must be an integer")

        with self.assertRaises(TypeError) as cm:
            sqr = Square(1, 2, "Bob")
        self.assertEqual(str(cm.exception), "y must be an integer")

    def test_value_errors_for_properties(self):
        with self.assertRaises(ValueError) as cm:
            sqr = Square(0, 1, 1)
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(ValueError) as cm:
            sqr = Square(-1, 1, 1)
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(ValueError) as cm:
            sqr = Square(1, -1, 1)
        self.assertEqual(str(cm.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as cm:
            sqr = Square(1, 1, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")
