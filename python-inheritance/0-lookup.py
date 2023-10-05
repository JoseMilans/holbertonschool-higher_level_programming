#!/usr/bin/python3
"""This module contains the lookup function."""


def lookup(obj):
    """
    Function that returns the list of available attributes and methods of
    an object.
    """
    return dir(obj)
