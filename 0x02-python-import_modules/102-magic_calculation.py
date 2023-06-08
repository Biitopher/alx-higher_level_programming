#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    c = a - b
    if c < 0:
        return c
    else:
        return c * 2
