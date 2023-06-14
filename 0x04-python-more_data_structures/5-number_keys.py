#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    result_keys = list(a_dictionary.keys())
    for x in result_keys:
        count += 1
    return count
