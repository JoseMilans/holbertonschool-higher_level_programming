#!/usr/bin/python3
"""
Module introducing a function which writes a string to a text file (UTF8).
"""


def write_file(filename="", text=""):
    """
    Writes a given text into a file and returns the number of characters
    written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
