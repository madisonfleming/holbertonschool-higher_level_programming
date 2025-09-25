#!/usr/bin/python3
"""
This module will includes one Animal class
with two Animal subclasses
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    This is a Shape class of abstract method
    """
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    """
    """
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(value):
    print("Area: {}\nPerimeter: {}".format(value.area(), value.perimeter()))
