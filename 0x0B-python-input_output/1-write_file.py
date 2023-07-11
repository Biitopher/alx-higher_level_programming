#!/usr/bin/python3
"""Defines function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Represents file writing"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
