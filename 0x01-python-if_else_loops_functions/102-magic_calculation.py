#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return a + b + c
    elif a > b and c != 0:
        return (a - b) / c
    else:
        return a * b - c
