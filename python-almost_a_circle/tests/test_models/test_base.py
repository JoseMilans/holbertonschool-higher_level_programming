#!/usr/bin/python3

import unittest
import json
from models.rectangle import Rectangle
Base = __import__('models.base').base.Base


"""Unit tests for Base class"""


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_auto_id_increment(self):
        auto_obj = Base()
        self.assertEqual(auto_obj.id, 1)

    def test_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)

    def test_id_assign(self):
        base_obj = Base(88)
        self.assertEqual(base_obj.id, 88)

    def test_to_json_str_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_str_empty_lst(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_str_valid_input(self):
        rect_obj = Rectangle(11, 6, 3, 9, 9)
        output = '[{"id": 9, "height": 6, "width": 11, "x": 3, "y": 9}]'
        dict_repr = rect_obj.to_dictionary()
        self.assertEqual(Base.to_json_string([dict_repr]), output)

    def test_to_json_str_invalid_input(self):
        output = Base.to_json_string("simple_str_not_a_list.")
        expec_output = json.dumps("simple_str_not_a_list.")
        self.assertEqual(output, expec_output)

    def test_from_json_str_invalid_input(self):
        with self.assertRaises(ValueError):
            _ = Base.from_json_string("not_JSON_str.")

    def test_negative_id(self):
        base_neg = Base(-1)
        self.assertEqual(base_neg.id, -1)

    def test_str_id(self):
        base_str = Base("str_id")
        self.assertEqual(base_str.id, "str_id")

    def test_float_id(self):
        base_float = Base(5.5)
        self.assertEqual(base_float.id, 5.5)

    def test_nb_objects_increment(self):
        _ = Base()
        _ = Base()
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_create_method_invalid_attrs(self):
        r1 = Rectangle(5, 5)
        r1_dict = r1.to_dictionary()
        r1_dict["invalid_attr"] = 6666
        r2 = Rectangle.create(**r1_dict)
        self.assertFalse(hasattr(r2, "invalid_attr"))

    def test_load_from_non_existent_file(self):
        output = Base.load_from_file()
        self.assertEqual(output, [])
