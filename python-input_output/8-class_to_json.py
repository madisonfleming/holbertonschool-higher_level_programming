#!/usr/bin/python3
"""
This module returns the dictionary description
with simple data structure for a json
serialisation of an object
"""


def class_to_json(obj):
    """
    this function will return a structure for a
    json serialisation of an object

    Attributes:
        obj: an instance of a class
    """
    return (obj.__dict__)
