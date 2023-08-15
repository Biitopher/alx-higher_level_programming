#!/usr/bin/python3


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_to_json_string(self):
        input_list = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        expected_output = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        self.assertEqual(Base.to_json_string(input_list), expected_output)

        self.assertEqual(Base.to_json_string([]), '[]')

        self.assertEqual(Base.to_json_string(None), '[]')

    def test_from_json_string(self):
        input_json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        expected_output = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        self.assertEqual(Base.from_json_string(input_json_string), expected_output)

        self.assertEqual(Base.from_json_string(''), [])

        self.assertEqual(Base.from_json_string(None), [])

