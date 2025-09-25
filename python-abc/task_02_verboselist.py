#!/usr/bin/python3
"""
This module includes one class VerboseList that
extends the python list class
"""


class VerboseList(list):
    """
    """

    def __init__(self, ml):
        super().__init__(ml if ml is not None else [])
        self.ml = ml

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items".format(len(item)))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list".format(item))

    def pop(self, index=-1):
        new_pop = super().pop(index)
        print("Popped [{}] from the list".format(new_pop))
