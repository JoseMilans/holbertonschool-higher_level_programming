#!/usr/bin/python3
"""
Module to save an object into a file using its JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """Serialise an object and save it to a file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
