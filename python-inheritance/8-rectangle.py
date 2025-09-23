#!/usr/bin/python3
"""
This module includes a parent class and subclass
"""


from base_geometry import BaseGeometry


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
