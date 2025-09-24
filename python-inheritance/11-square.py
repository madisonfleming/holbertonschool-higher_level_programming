#!/usr/bin/python3
"""
This module imports a parent class and creates a subclass
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is a subclass of Rectangle
    Args:
        size: private attribute
    """
    def __init__(self, size):
        """
        Initialises a new instance of Square

        Args:
            size: int value
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
