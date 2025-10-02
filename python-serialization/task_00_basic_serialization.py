#!/usr/bin/env python3
"""
This module serialises a python dict to
json file
and deserialise the json file to recreate the dict
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    This function serialises and saves data
    to the filename
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    This function loads and deserialises data from
    the json file
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data
