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
