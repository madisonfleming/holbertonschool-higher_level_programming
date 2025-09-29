#!/usr/bin/python3
"""
This module returns the dictionary description
with simple data structure for a json
serialisation of an object
"""


import json


def class_to_json(obj):
    """
    this function will return a structure for a
    json serialisation of an object

    Attributes:
        obj: an instance of a class
    """
    return json.dumps(obj.__dict__)
