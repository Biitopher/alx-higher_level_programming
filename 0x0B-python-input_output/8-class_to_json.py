#!/usr/bin/python3
"""Defines function that returns dictionary description"""


def class_to_json(obj):
    """Represents class to json"""
    return obj.__dict__
