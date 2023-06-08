#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a > b:
        return (a - b)
        if a < b:
            return (a + b) * 2
        else:
            return (a * b) ** 2
