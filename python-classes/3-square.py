#!/usr/bin/python3
"""This module defines a class Square that represents a square with
   its properties and behaviors."""


class Square:
    """The class is constructed with an optional size attribute which
       is validated,and includes a method to compute the square area."""
    def __init__(self, size=0):
        """Initialises a square instance.
        Args:
            size (int): square size, must be >= 0.
        Raises:
            TypeError: size isn't an int.
            ValueError: size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes the square area.
        Returns:
            The square area.
        """
        return self.__size * self.__size
