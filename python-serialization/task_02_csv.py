#!/usr/bin/python
"""
Read data from CSV format and convert to JSON format
using serialization
"""


import csv
import json


def convert_csv_to_json(filename):
    """
    take a csv file and write to
    a json file
    """
    rows = []
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                rows.append(row)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
            return True
    except FileNotFoundError:
        return False
