#!/usr/bin/python3
"""Defines lookup function"""


def lookup(obj):
    """Return list"""
    return sorted(dir(obj))
