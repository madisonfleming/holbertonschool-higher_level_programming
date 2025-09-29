#!/usr/bin/python3
"""
This module write a string to a text file and
returns the number of characters
"""


def write_file(filename="", text=""):
    """
    This function opens a file, writes text to it

    Returns: number of characters printed
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
