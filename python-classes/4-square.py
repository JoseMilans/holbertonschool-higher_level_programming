#!/usr/bin/python3
"""This module contains a class Square that defines a square."""


class Square:
    """Represents a square with properties."""

    def __init__(self, size=0):
        """Initialises square instance.
        Args:
            size (int): Square's size, must be >= 0.
        The initialiser also serves as a checker for the input.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to catch the size of the square.

        Returns:
            Square size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method, sets square size including a validation.
        Args:
            value (int): New square size.
        Raises:
            TypeError: If it isn't an int.
            ValueError: If it's < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes square's area.
        Returns:
            The square area.
        """
        return self.__size * self.__size
