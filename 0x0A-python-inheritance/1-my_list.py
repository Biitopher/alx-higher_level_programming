#!/usr/bin/python3
"""Defines inherits from list"""


class MyList(list):
    """Represents MyList"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
