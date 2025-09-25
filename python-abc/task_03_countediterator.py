#!/usr/bin/python3
"""
This module will includes one Animal class
with two Animal subclasses
"""


class CountedIterator:
    """
    """
    def __init__(self, some_iterable):
        self.items = list(some_iterable)
        self.iterator = iter(some_iterable)
        self.count = 0

    def __iter__(self):
        return self

    def get_count(self):
        return self.count

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item
