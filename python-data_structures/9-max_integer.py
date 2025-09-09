#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = my_list[0]
    if largest == 0:
        return None
    for val in my_list:
        if val > largest:
            largest = val
    return largest
