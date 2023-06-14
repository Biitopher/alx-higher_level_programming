#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order_list = list(a_dictionary.keys())
    order_list.sort()
    for x in order_list:
        print("{}: {}".format(x, a_dictionary.get(x)))    
