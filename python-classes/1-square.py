#!/usr/bin/python3
"""This module defines a class Square with a private attribute size."""


class Square:
    """This class represents a geometric square,
    and is constructed with a size attribute"""
    def __init__(self, size):
        """Initialises the Square instance with a given size.
        Args:
            size (int): size of the square.
        """
        self.__size = size
