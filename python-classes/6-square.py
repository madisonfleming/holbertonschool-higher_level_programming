#!/usr/bin/python3
"""This is a square class
"""


class Square:
    """A square

    Attributes:
        size: size of the square
    """
    __size = 0

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(' ' * self.position[0] + '#' * self.size)
