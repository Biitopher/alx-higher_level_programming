#!/usr/bin/python3
"""Defines square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Overriding of the string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Handles arguments"""
        if args:
            arg_names = ['id', 'size', 'x', 'y']
            for a, arg in enumerate(args):
                setattr(self, arg_names[a], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Represents dictionary"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
