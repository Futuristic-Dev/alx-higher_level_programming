#!/usr/bin/python3

"""
Unittest for Base class.

Run with python3 -m unittest discover tests
Run with python3 -m unittest tests/test_models/test_base.py
"""

import os
import unittest
import json
from models import base
from models import rectangle
from models import square
Base = base.Base
Rectangle = rectangle.Rectangle
Square = square.Square



class TestBase(unittest.TestCase):
    """TestBase class."""

    def test_module_docstring(self):
        """Test if the module docstring is present."""
        self.assertTrue(len(__doc__) >= 1)

    def test_class_docstring(self):
        """Validate if the Base class docstring is  present."""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_id_assignment_with_id_argument(self):
        """
        Validate if the id attribute is assigned correctly when no id.\n
        Argument id provided.
        """
        base_instance = Base()
        base_instance2 = Base()

        self.assertEqual(base_instance.id, 3)
        self.assertEqual(base_instance2.id, 4)

    def test_id_assignment_with_string(self):
        """Validate if the id attribute would work correctly."""
        base_string = Base("Webinar")
        self.asserEqual(base_string.id, "Webinar")
        base_string2 = Base("Unittest")
        self.assertEqual(base_string2.id, "Unittest")

    def test_more_than_one_arg(self):
        """
        Validate if Base class does raise the TypeError if more than.\n
        One arg is passed as id.
        """
        with self.assertRaises(TypeError):
            Base(42, 25)

    def test_type(self):
        self.assertEqual(type(Base), type)

    def test_id_reassignment(self):
        """
        Validate if id can be reassigned a new value after\n
        Initialization.
        """
        switch = Base(25)
        switch.id = 42
        self.assertEqual(42, switch.id)

    def test_to_json_string(self):
        list_of_dicts = [
                {'id': 1, 'name': 'Joy'},
                {'id': 2, 'name': 'Bob'},
                ]
        output = '[{"id": 1, "name": "Joy"}, {"id": 2, "name": "Bob"}]'
        result = Base.to_json_string(list_of_dicts)
        self.assertTrue(type(result) == str)

    def test_to_json_string_empty_list(self):
        list_of_dicts = []
        expected_output = '[]'
        json_str = Base.to_json_string(list_of_dicts)
        self.assertequal(json_str, expected_output)

    def test_to_json_string_none(self):
        list_of_dicts = None
        expected_output = '[]'
        json_str = Base.to_json_string(list_of_dicts)
        self.assertEqual(json_str, expected_output)

    def test_save_to_file(self):
        """
        Test save to file with instance that inherited from Base.
        """
        r = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.dumps([r.to_dictionary(), r2.to_dictionary()]),
                    file.read())

    def test_save_to_file_empty_list(self):
        """Test if empty list is given to be saved."""
        list_of_objs = []
        filename = 'Rectangle.json'
        Rectangle.save_to_file(list_of_objs)
        with open(filename, 'r') as my_file:
            saved_data = my_file.read()
        expected_data = '[]'
        self.assertEqual(saved_data, expected_data)

    def test_from_json_string(self):
        """Test that checks the methods basic functionality with JSON string."""
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        json_output = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        result = Base.from_json_string(json_string)
        self.assertEqual(result, json_output)
        json_string = '[
        {"id": 9, "height": 6, "x": 7, "y": 8},
        {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        ]'
        json_output = Base.from_json_string(json_string)
        self.assertEqual(len(json_output), 2)
        self.assertTrue(type(json_output), is list)
        self.assertTrue(type(json_output[0]) is dict)
        self.assertTrue(type(json_output[1]) is dict)
        self.assertEqual(json_output[0],
                {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(jso_output[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

        def test_from_json_string_empty_string(self):
            """Test that validates an empty string."""
            json_string = ' '
            json_output = []
            result = Base.from_json_ string(json_string)
            self.assertEqual(result, json_output)

        def test_from_json_string_none(self):
            """Test to validate the method's functionality for creating instances of 
            Rectangle class."""
            dictionary = {'id': 42, 'width': 4, 'height': 3, 'x': 2, 'y': 1}
            r = Rectangle.create(**dictionary)
            self.assertIsInstance(r, Rectangle)
            self.assertIsInstance(r.id, 42)
            self.assertEqual(r.width, 4)
            self.assertEqual(r.height, 3)
            self.assertEqual(r.x, 2)
            self.assertEqual(r.y, 1)






