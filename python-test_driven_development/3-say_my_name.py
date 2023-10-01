#!/usr/bin/python3
"""
    Module to define say_my_name function that prints
    the full name passed as parameters.
"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name (str): The forename.
        last_name (str):  The surname.
    Raises:
        TypeError: If first_name or last_name aren't strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
