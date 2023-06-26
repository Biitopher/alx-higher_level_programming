#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0

    try:
        for element in my_list:
            if num < x:
                print(element, end='')
                num += 1
    except TypeError:
        pass
    finally:
        print()
        return num
