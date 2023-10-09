#!/usr/bin/python3
"""Module to define Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base.

    Attrs:
        width (int)
        height (int)
        x (int)
        y (int)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method for Rectangle class.

        Args:
            width (int)
            height (int)
            x (int)
            y (int)
            id (int)
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set rectangle height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set and validate x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set and validate y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return rectangle area."""
        return self.width * self.height

    def display(self):
        """Print rectangle using # character"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Return formatted string"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.
        Args order: id, width, height, x, y.
        If args is empty, check kwargs.
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for i in range(len(args)):
                if i < len(attributes):
                    setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
