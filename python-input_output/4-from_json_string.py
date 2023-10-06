#!/usr/bin/python3
"""
Module to convert a JSON string to an object.
"""


import json


def from_json_string(my_str):
    """
    Convert a JSON string to its Python data structure.
    """
    return json.loads(my_str)
