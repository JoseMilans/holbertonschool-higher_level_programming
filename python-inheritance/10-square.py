#!/usr/bin/python3
"""Define the Square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square which is a special kind of Rectangle."""

    def __init__(self, size):
        """Initialise the Square."""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
