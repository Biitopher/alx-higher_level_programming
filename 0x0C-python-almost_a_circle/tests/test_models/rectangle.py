#!/usr/bin/python3

import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 5 * 10)

    def test_display(self):
        expected_output = "##\n" * 10
        self.rectangle.display()


    def test_str(self):
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(self.rectangle), expected_output)

    def test_update(self):
        self.rectangle.update(2, 7, 8, 4, 5)
        self.assertEqual(self.rectangle.width, 7)
        self.assertEqual(self.rectangle.height, 8)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 5)
        self.assertEqual(self.rectangle.id, 2)

    def test_to_dictionary(self):
        expected_dict = {
            'id': 1,
            'width': 5,
            'height': 10,
            'x': 2,
            'y': 3
        }
        self.assertEqual(self.rectangle.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()

