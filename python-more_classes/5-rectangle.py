#!/usr/bin/python3
"""This is a rectangle class
"""


class Rectangle:
    """
    Rectangle class

    Args:
        width: width of the rectangle
        height: height of the rectangle

    Raises:
        TypeError: if width or height are not integers
        ValueError: if width or height are less than 0
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        print_str = ""
        for _ in range(self.__height):
            print_str += '#' * self.__width + '\n'

        return print_str.rstrip()

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
