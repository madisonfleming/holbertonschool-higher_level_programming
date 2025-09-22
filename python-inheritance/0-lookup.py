#!/usr/bin/python3
class object:
    """
    This is a parent class

    Attributes:
        my_attr1: single attribute
    """
def lookup(obj):
    """
    A new instance of object to return the
    attributes and methods of a class

    Args:
        obj: the object to lookup
    """
    return dir(obj)
