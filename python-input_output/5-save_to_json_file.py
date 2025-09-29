#!/usr/bin/python3
"""
Write an object to a text file using json
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Open a file and write to it with an object
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
