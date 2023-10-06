#!/usr/bin/python3
"""
Module to get the JSON representation of an object (string).
"""

import json


def to_json_string(my_obj):
    """Return the JSON format of an object."""
    return json.dumps(my_obj)
