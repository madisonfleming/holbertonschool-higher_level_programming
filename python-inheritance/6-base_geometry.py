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
