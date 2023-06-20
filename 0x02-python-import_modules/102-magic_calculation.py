#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    c = 0
    add, sub = magic_calculation_102.add, magic_calculation_102.sub
    if a < b:
        c = add(a, b)
        for x in range(4, 6):
            c = add(c, x)
            return (c)
        else:
            return (sub(a, b))
