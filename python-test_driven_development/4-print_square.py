#!/usr/bin/python3
"""
Module containing a function to print a square.
"""


def print_square(size):
    """
    This function prints a square with the character '#'.
    Args:
        size (int): The square size.
    Raises:
        TypeError: If size is not an int.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for _ in range(size):
        print("#" * size)
