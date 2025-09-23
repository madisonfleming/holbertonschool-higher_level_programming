#!/usr/bin/python3
"""
This module includes a single class
"""


class BaseGeometry:
    """
    This is a BaseGeometry class

    Raises:
        Exception: area() is not implemented
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.value = value
        self.name = name
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
