#!/usr/bin/python3
"""
This module returns the dictionary description
with simple data structure for a json
serialisation of an object
"""


class Student:
    """
    This is a Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(obj):
        """
        this function will return a structure for a
        json serialisation of an object

        Attributes:
            obj: an instance of a class
        """
        return (obj.__dict__)
