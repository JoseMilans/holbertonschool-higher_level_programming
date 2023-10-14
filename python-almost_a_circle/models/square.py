#!/usr/bin/python3
"""Module to define Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method for Square class.

        Args:
            size (int)
            x (int)
            y (int)
            id (int)
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return formatted string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get square size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set square size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update square attrs using args or kwargs.
        args order: id, size, x, y.
        args takes priority over kwargs.
        """
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for idx, val in enumerate(args):
                if idx < len(attrs):
                    setattr(self, attrs[idx], val)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
