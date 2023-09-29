#!/usr/bin/python3
"""This module defines a class Square that represents a geometric square."""


class Square:
    """This class represents a geometric square and its properties."""
    def __init__(self, size=0):
        """Initialises a Square instance with a validated size.
        Args:
            size (int): square size, must be an int and >= 0.
        Raises:
            TypeError: if size is't an int.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
