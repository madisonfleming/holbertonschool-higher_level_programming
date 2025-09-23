#!/usr/bin/python3
"""
This module will check the instance of an object
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class
    that inherited directly or indirectly from the
    specified class

    Args:
        obj: object to check
        a_class: class to compare
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
