#!/usr/bin/python3
"""Defines function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Represents appended file"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
