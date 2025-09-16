#!/usr/bin/python3
"""
This module contains one function for adding two integers together
"""


def add_integer(a, b=98):
    """ Return sum of two integers

    Args:
        a: The first integer
        b: the second integer

    Returns:
        sum of a and b

    Raises:
        TypeError: if a or b are not integers or floats
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")

    if b is None or (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
