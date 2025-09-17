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
    d = {'. ': '.\n\n', '? ': '?\n\n', ': ': ':\n\n'}
    result = text
    for key, value in d.items():
        result = result.replace(key, value)
    print("{}".format(result), end="")
