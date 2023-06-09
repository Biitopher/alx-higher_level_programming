#!/usr/bin/python3
"""Defines function that writes an Object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """Represents save to json file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
