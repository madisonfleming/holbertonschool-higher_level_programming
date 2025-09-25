#!/usr/bin/python3
"""
This module will includes one Animal class
with two Animal subclasses
"""


class CountedIterator:
    """
    """
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.count = 0

    def __iter__(self):
        for item in self.items:
            yield item

    def get_count(self):
        return self.count

    def __next__(self):
        self.__next__ = next
        self.count += 1
        for item in self.iterator:
            return item
        else:
            raise StopIteration
