#!/usr/bin/python3
"""Module to define the Student class."""


class Student:
    """Represents a student with name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialises student obj."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(item, str)
                                           for item in attrs):
            stud_attrs = self.__dict__
            return {key: stud_attrs[key]
                    for key in attrs if key in stud_attrs}

        return self.__dict__
