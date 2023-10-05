#!/usr/bin/python3
"""Module containing MyList class."""


class MyList(list):
    """MyList is a subclass of the built-in list."""
    def print_sorted(self):
        """Prints the elements of the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
