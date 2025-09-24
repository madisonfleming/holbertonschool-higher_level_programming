#!/usr/bin/python3
"""
This module will includes one Animal class
with two Animal subclasses
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    This is an animal class of abstract method
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    This is a Dog subclass of Animal
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    This is a Cat subclass of Animal
    """
    def sound(self):
        return "Meow"
