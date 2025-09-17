#!/usr/bin/python3
"""
This module includes one function to print a square
"""


def print_square(size):
    """
    Prints a square
    Args:
        size: the size length of the square

    Raises:
        TypeError: if size if not an int or is a float and less than 0
        ValueError: if size is less than 0
    """
    if size is None or type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print("#", end="")
        print()
