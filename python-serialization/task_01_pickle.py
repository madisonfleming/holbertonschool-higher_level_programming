#!/usr/bin/python
"""
This module will serialise and deserialise
custom python objects using pickle
"""


import pickle


class CustomObject:
    """
    """
    def __init__(self, name="", age=1, is_student=True):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        print the objects attributes
        """
        print("Name: {}\nAge: {}\nIs Student: {}"
              .format(self.name, self.age, self.is_student))

    def serialize(self, filename):
        """
        use pickle to serialise the current instance of the object
        and save to the provided filename
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (EOFError, pickle.UnpicklingError, FileNotFoundError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Use pickle to load and return an instance
        of the customobject from the filename
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    return None
        except (EOFError, pickle.UnpicklingError, FileNotFoundError):
            return None
