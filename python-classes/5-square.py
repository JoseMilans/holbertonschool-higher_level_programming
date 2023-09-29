#!/usr/bin/python3
"""This module contains a class Square that defines a square."""


class Square:
    """Represents a square with properties."""

    def __init__(self, size=0):
        """Initialises Square instance.
        Args:
            size (int): Square's size, must be >= 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square.
        Returns:
            Square size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with value.
        Args:
            value (int): New square size.
        Raises:
            TypeError: If it isn't an int.
            ValueError: If it's < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes square area.
        Returns:
            The square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the char '#' or
        an empty line if size is 0"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size, end="")
                print()
