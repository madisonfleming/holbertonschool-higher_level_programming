#!/usr/bin/python3
"""
This module will check the instance of an object
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of the class
    that inherited from the specified class

    Args:
        obj: object to check
        a_class: class to compare
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
