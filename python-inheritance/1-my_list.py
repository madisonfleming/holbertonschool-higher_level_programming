#!/usr/bin/python3
"""
This module includes a class that is inherited from list.
"""


class MyList(list):
    """
    Mylist is a subclass of list
    """

    def print_sorted(self):
        """
        Print list in ascending order
        """
        print(sorted(self))
