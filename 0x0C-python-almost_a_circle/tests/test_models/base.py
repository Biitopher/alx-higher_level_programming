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

    def test_save_to_file(self):
        class MockObj:
            def to_dictionary(self):
                return {'id': 1, 'name': 'Test'}

        mock_objs = [MockObj(), MockObj(), MockObj()]
        Base.save_to_file(mock__objs)


if __name__ == '__main__':
    unittest.main()
