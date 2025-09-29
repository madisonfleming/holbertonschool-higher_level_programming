#!/usr/bin/python3
"""
This module reads a text file and prints it
"""


def read_file(filename=""):
    """
    This function will open and read a file
    and print line by line
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
