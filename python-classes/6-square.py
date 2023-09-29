#!/usr/bin/python3
"""This module contains a class Square that defines a square."""


class Square:
    """Represents a square with properties."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialises Square instance.
        Args:
            size (int): Square's size, must be >= 0.
            position (tuple): Square position.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square that  must be a tuple of 2 positive
        integers with value.
        """
        msg = "position must be a tuple of 2 positive integers"
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError(msg)
        self.__position = value

    def area(self):
        """Computes square area.
        Returns:
            The square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the char '#'
        considering its position or an empty line if size is 0"""
        if self.__size == 0:
            print()
            return
        print('\n' * self.__position[1], end="")
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
