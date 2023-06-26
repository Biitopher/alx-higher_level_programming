#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0

    try:
        for element in my_list:
            if isinstance(element, int):
                print("{:d}".format(element), end='')
                num += 1
                if num == x:
                    break
                except TypeError:
                    pass
                finally:
                    print()
                    return num
