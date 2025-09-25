#!/usr/bin/python3
"""
This module will includes two parent classes or
mixins and one subclass
"""


class SwimMixin:
    """
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    """
    def roar(self):
        print("The dragon roars!")
