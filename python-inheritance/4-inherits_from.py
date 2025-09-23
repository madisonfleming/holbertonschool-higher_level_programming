#!/usr/bin/python3
"""
This module will check the instance of an object
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of the class
    that inherited directly or indirectly from the specified class

    Args:
        obj: object to check
        a_class: class to compare
    """
    if obj.__class__ is not a_class:
        return True
    else:
        return False
