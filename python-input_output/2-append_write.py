#!/usr/bin/python3
"""
Module for appending strings to a text file (UTF8).
"""


def append_write(filename="", text=""):
    """
    Appends a given text at the end of a file and returns
    the number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
