#!/usr/bin/python3
"""Module introducing the BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with methods and attributes."""

    def area(self):
        """Method that raises an exception with a specific message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
