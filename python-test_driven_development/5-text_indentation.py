#!/usr/bin/python3
"""
This module includes one function to indent text after ., ?, :
"""


def text_indentation(text):
    """
    Print text with 2 newlines after . ? :

    Args:
        text: a string to indent

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = text
    for char in ['.', '?', ':']:
        result = result.replace(char, char + '\n\n')

    lines = result.split('\n')
    for line in lines:
        line = line.strip()
        if line:
            print(line)
            print()
