#!/usr/bin/python3
"""Module to create an object from a JSON file."""


import json


def load_from_json_file(filename):
    """Read a JSON file and return its object."""

    with open(filename, 'r') as f_obj:
        return json.load(f_obj)
