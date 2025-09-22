#!/usr/bin/python3
"""
    This is a function that returns a list
    of available attributes and methods of an object
"""


def lookup(obj):
    """
    Return the attributes and methods of an object

    Args:
        obj: the object to lookup
    """
    return dir(obj)
