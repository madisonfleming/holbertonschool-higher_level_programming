#!/usr/bin/python3
"""
This module appends a string to the end of
a text file
"""


def append_write(filename="", text=""):
    """
    This function opens a file and appends text

    Returns: number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
