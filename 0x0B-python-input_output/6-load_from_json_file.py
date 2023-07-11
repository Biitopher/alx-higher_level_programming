#!/usr/bin/python3
"""Defines a function that creates an Object from a JSON file"""


import json

def load_from_json_file(filename):
    """Represents json file from load"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
