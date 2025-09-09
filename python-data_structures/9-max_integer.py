#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    largest = my_list[0]
    for val in my_list:
        if val > largest:
            largest = val
    return largest
