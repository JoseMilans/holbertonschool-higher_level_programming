#!/usr/bin/python3
"""Module for representing students."""


class Student:
    """Represents a student with a name and age."""
    def __init__(self, first_name, last_name, age):
        """Initialises student obj."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.
        """
        return self.__dict__
