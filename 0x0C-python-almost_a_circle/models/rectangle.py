#!/usr/bin/python3
"""Defines a rectangle"""


from models.base import Base


class Rectangle(Base):
    """"Represents rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
