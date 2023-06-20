#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    list = 0
    for x in unique:
        list += x
    return(list)
