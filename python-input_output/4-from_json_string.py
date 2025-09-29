#!/usr/bin/python3
"""
This module return an object
represented by a json string
"""


import json


def from_json_string(my_str):
    """
    This function returns an object
    representated by a json string
    """
    list = json.loads(my_str)
    return list
