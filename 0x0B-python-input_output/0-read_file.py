#!/usr/bin/python3
"""Defines function that reads a text file"""


def read_file(filename=""):
    """Represents file read"""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
