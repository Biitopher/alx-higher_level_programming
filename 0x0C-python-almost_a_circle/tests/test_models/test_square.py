#!/usr/bin/python3

import unittest
import io
import sys
from models.base import Base
from models.square import Square


class SquareTestCase(unittest.TestCase):
    def setUp(self):
        """Create an instance of the Square class"""
        self.square = Square(5, 2, 3, 1)

    def test_size(self):
        """Test the getter and setter for the size property"""
        self.assertEqual(self.square.size, 5)
        self.square.size = 10
        self.assertEqual(self.square.size, 10)

    def test_string_representation(self):
        """Test the __str__()"""
        self.assertEqual(str(self.square), "[Square] (1) 2/3 - 5")

    def test_update(self):
        """Test the update() method with positional arguments"""
        self.square.update(2, 8, 4, 6)
        self.assertEqual(str(self.square), "[Square] (2) 4/6 - 8")

        self.square.update(x=1, y=2, size=7)
        self.assertEqual(str(self.square), "[Square] (2) 1/2 - 7")

    def test_to_dictionary(self):
        """Test the to_dictionary() method"""
        expected_dict = {
            'id': 1,
            'size': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(self.square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
