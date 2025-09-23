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


class Rectangle(BaseGeometry):
    """
    This is a subclass of BaseGeometry
    Args:
        width: private attribute
        height: private attribute
    """
    def __init__(self, width, height):
        """
        Initialises a new instance of Rectangle

        Args:
            width: int value
            height: int value
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
