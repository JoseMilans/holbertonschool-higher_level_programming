#!/usr/bin/python3
"""
Module containing a function to check if an object
is an instance of a specific class.
"""


def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class.
    """
    return type(obj) == a_class
