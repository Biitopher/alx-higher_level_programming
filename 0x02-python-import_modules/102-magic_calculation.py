#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for x in range(4, 6):
            c = add(c, x)
            return (c)
        else:
            return (sub(a, b))


print(dis.dis(magic_calculation))
