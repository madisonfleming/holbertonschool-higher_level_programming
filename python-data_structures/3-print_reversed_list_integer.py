#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse = list(reversed(my_list))
    for i in reverse:
        print("{:d}".format(i, end=""))
