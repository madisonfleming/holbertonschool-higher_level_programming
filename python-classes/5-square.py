#!/usr/bin/python3
"""This is a square class
"""


class Square:
    """A square

    Attributes:
        size: size of the square
    """
    __size = 0

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        char = '#'
        for _ in range(self.size):
            print((char) * self.size)
        if self.size is 0:
            print("\n")
