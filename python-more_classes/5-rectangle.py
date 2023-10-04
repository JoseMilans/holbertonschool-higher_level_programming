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
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute and return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Compute and return rectangle perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Return a string representation of the rectangle using '#'."""
        if self.height == 0 or self.width == 0:
            return ""
        rows = ['#' * self.width for _ in range(self.height)]
        return '\n'.join(rows)

    def __repr__(self):
        """Return a string that can recreate the rectangle using eval()."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when an instance is deleted."""
        print("Bye rectangle...")
