#!/usr/bin/python3
"""
This module creates an Object from a json file
"""


import json


def load_from_json_file(filename):
    """
    This function opens and creates a new object
    from a json file
    """
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)
        return obj
