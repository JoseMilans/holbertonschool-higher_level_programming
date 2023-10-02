#!/usr/bin/python3
"""
This module contains a function that indents text
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Args:
        text (str): The text to format.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    formatted_text = ''
    skip_space = False
    for char in text:
        if skip_space and char == ' ':
            continue
        elif char in ['.', '?', ':']:
            formatted_text += char + '\n\n'
            skip_space = True
        else:
            formatted_text += char
            skip_space = False
    print(formatted_text, end="")
