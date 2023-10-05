#!/usr/bin/python3
"""
Module containing a function to check if an object
is an instance of a specific class or inherits
attributes of the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of a specific
    class or has inherited attributes of it.
    """
    result = isinstance(obj, a_class)
    return result
