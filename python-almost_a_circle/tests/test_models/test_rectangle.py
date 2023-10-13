#!/usr/bin/python3
"""Unit tests for Rectangle subclass"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rect_width_attr(self):
        rect = Rectangle(5, 6)
        self.assertEqual(rect.width, 5)
        rect.width = 7
        self.assertEqual(rect.width, 7)

    def test_rect_height_attr(self):
        rect = Rectangle(5, 6)
        self.assertEqual(rect.height, 6)
        rect.height = 8
        self.assertEqual(rect.height, 8)

    def test_rect_x_attr(self):
        rect = Rectangle(5, 6, 2, 3)
        self.assertEqual(rect.x, 2)
        rect.x = 9
        self.assertEqual(rect.x, 9)

    def test_rect_y_attr(self):
        rect = Rectangle(5, 6, 2, 3)
        self.assertEqual(rect.y, 3)
        rect.y = 10
        self.assertEqual(rect.y, 10)

    def test_width_type_error_with_string(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("Tito", 3)

    def test_height_type_error_with_string(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(3, "Bob")

    def test_width_value_error_with_zero(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 3)

    def test_height_value_error_with_zero(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 0)

    def test_rectangle_area(self):
        rect = Rectangle(3, 3)
        self.assertEqual(rect.area(), 9)

    def test_override_str_method(self):
        rect = Rectangle(3, 4, 5, 6, 8)
        self.assertEqual(rect.__str__(), "[Rectangle] (8) 5/6 - 3/4")

    def test_rectangle_display(self):
        rect = Rectangle(4, 3, 2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), "\n\n  ####\n  ####\n  ####\n")

    def test_rect_update(self):
        rect = Rectangle(3, 3, 2, 2)
        rect.update(id=45, width=5, height=5, x=3, y=3)
        self.assertEqual(rect.__str__(), "[Rectangle] (45) 3/3 - 5/5")

    def test_rect_update_from_dict(self):
        rect = Rectangle(3, 3, 2, 2)
        rect.update(x=2, height=3, y=4, width=5, id=265)
        self.assertEqual(rect.__str__(), "[Rectangle] (265) 2/4 - 5/3")

    def test_base_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_id_assignment(self):
        rect = Rectangle(5, 6, 1, 2, 77)
        self.assertEqual(rect.id, 77)

    def test_width_type_error_with_string(self):
        with self.assertRaises(TypeError) as exc:
            rect = Rectangle("RectangleStr", 2, 3, 4)
            self.assertEqual(str(exc.exception), "width must be a valid integer")

    def test_width_value_error_negative(self):
        with self.assertRaises(ValueError) as exc:
            rect = Rectangle(-6, 3, 3, 4)
            self.assertEqual(str(exc.exception), "width must be greater than 0")

    def test_height_value_error_negative(self):
        """Test ValueError for height with negative value."""
        with self.assertRaises(ValueError) as exc:
            rect = Rectangle(2, -6, 3, 4)
            self.assertEqual(str(exc.exception), "height must be greater than 0")

    def test_rectangle_to_dictionary(self):
        """Test conversion of Rectangle attributes to dictionary."""
        rect = Rectangle(11, 3, 2, 10, 8)
        output = {'x': 2, 'y': 10, 'id': 8, 'height': 3, 'width': 11}
        self.assertEqual(rect.to_dictionary(), output)
