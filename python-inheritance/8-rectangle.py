#!/usr/bin/python3
"""Module introducing the BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class is a subclass of BaseGeometry."""
    def __init__(self, width, height):
        """Initialises the rectangle, validating width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
