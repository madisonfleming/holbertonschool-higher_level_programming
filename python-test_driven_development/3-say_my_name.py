#!/usr/bin/python3
"""
This module includes one function to print a name
"""


def say_my_name(first_name, last_name=""):
    """print first and last name

    Args:
        first_name - first argument to print
        last_name - second argument to print

    Raise:
        TypeError: if arguments are not strings
    """
    if first_name is None or (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if last_name is None or (type(last_name) is not str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
