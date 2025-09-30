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

    def to_json(self, attrs=None):
        """
        this function will return a structure for a
        json serialisation of an object

        Attributes:
            attrs: if a list of strings, only
            attribute names must be retrieved,
            otherwise retrieve all attributes
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            if hasattr(self, k):
                setattr(self, k, v)
