#!/usr/bin/python3
"""
This module will check the instance of an object
"""


def is_same_class(obj, a_class):
    """
    Check if the object is the exact instance of the class

    Args:
        obj: object to check
        a_class: class to compare
    """
    if obj.__class__ is a_class:
        return True
    else:
        return False
