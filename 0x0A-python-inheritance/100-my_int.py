#!/usr/bin/python3
"""Defines class inherits from int"""


class MyInt(int):
    """Represents MyInt class"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
