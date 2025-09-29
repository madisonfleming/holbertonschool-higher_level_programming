#!/usr/bin/python3
"""
This module adds arguments to a python list
then saves them to a json file
"""


import sys
import json


def save_to_json_file(filename, arguments):
    """
    Open a file and write to it with an object
    """
    arguments = sys.argv[1:]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(arguments, f)


def load_from_json_file(filename):
    """
    This function opens and creates a new object
    from a json file
    """
    with open(filename, "r", encoding="utf-8") as f:
        json.load(f)


arguments = sys.argv[1:]
output_file = "add_item.json"
save_to_json_file(output_file, arguments)
