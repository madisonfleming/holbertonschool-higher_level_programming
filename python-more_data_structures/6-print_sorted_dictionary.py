#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    th_key = list(a_dictionary.keys())
    th_key.sort()
    sorted_dict = {i: a_dictionary[i] for i in th_key}
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
