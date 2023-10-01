#!/usr/bin/python3
"""This module contains a function that adds two integers."""


def add_integer(a, b=98):
    """
    Args:
        a (int or float): The first parametert.
        b (int or float): The second parameter.
    Returns:
        int: The addition of a and b.
    Raises:
        TypeError: If a or b isn't an int or a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
