#!/usr/bin/python3
"""Defines function that returns an object"""


import json


def from_json_string(my_str):
    """Represents json string"""
    return json.loads(my_str)
