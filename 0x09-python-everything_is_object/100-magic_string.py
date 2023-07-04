#!/usr/bin/python3
def magic_string():
    magic_string.b = magic_string.b + 1 if hasattr(magic_string, 'b') else 1
    return ', '.join(['BestSchool'] * magic_string.b)
