#!/usr/bin/python3
"""Defines new attribute"""


def add_attribute(obj, attr_name, attr_value):
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    obj.__setattr__(attr_name, attr_value)
