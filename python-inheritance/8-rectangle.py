#!/usr/bin/python3
"""
This module includes a parent class and subclass
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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    This is a subclass of BaseGeometry
    Args:
        width: private attribute
        height: private attribute
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
