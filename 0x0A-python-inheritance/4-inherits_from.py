#!/usr/bin/python3
"""Defines inherited class"""

def inherits_from(obj, a_class):
    """Represents inherits from"""
    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
    return False
