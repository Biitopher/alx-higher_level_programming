#!/usr/bin/python3

def safe_print_integer(value):
    try:
        integer_value = "{:d}".format(value)
        print(integer_value)
        return True
    except (ValueError, TypeError):
        return False
