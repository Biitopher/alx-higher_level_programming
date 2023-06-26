#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for element in range(0, x):
        try:
            print("{:d}".format(element), end='')
            num += 1
        except (ValueError, TypeError):
            continue
    print()
    return num
