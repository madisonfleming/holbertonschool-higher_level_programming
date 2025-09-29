#!/usr/bin/python3
"""
This module reads a text file and prints it
"""


def read_file(filename=""):
    """
    This function will open and read a file
    and print line by line
    """
    with open("my_file_0.txt", "r", encoding="utf-8") as filename:
        line = filename.read()
        print(line, end="")
