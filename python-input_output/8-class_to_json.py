#!/usr/bin/python3

"""
Module to represent an object in a format suitable for JSON serialisation.
"""


def class_to_json(obj):
    """
    Return a dictionary description with simple data structure of an object.
    """
    return obj.__dict__
