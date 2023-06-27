#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        raise TypeError("unsupported operand type(s) for >: 'Square' and '{}'".format(type(other).__name__))

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
        raise TypeError("unsupported operand type(s) for >=: 'Square' and '{}'".format(type(other).__name__))

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        raise TypeError("unsupported operand type(s) for <: 'Square' and '{}'".format(type(other).__name__))

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
        raise TypeError("unsupported operand type(s) for <=: 'Square' and '{}'".format(type(other).__name__))
