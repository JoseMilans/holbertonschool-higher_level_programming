#!/usr/bin/python3
"""
Module that checks if an object is an instance of a class
that has directly or indirectly inherited attributes of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that
    inherited attributes of the given class.
    """
    if isinstance(obj, a_class) and not type(obj) == a_class:
        return True
    return False
