#!/usr/bin/python3
"""
This module return the json
represeentation of an object (string)
"""


import json


def to_json_string(my_obj):
    """
    This function returns the json
    representation of an object

    Attributes: my_obj: object to convert
    Returns: json string
    """
    list = json.dumps(my_obj)
    return list
