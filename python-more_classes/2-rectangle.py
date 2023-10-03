#!/usr/bin/python3
"""Module to define a rectangle."""


class Rectangle:
    """A class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialises rectangle."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Return rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set rectangle height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute and return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Compute and return rectangle perimeter."""
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2
