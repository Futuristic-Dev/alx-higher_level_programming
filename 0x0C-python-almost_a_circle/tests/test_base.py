#!/usr/bin/python3

"""
unittest for a base class module.
>>run with pyhton3 -m unittest discover tests.
>>run with puthon3 -m unittest tests/test_models/test_base.py.
"""


import os
import unittest
import json
from models import base
from models import rectangle
from models import square

Base = base.Base
Rectangle = rectangle.Rectangle
square = square.Square



class TestBase(unittest.TestCase):
    """TestBase Class"""

    def test_module_docstring(self):
        """Test if the module docstring is present."""
        self.assertTrue(len(__doc__) >= 1)

    def test_class_docstring(self):
        """Test if the Base class docstring is present."""
        self.assertTrue(len(__doc_) >= 1)

    def test_id_assignment_with_id_argument(self):
        """Test to check whether the id attribute is assigned\n
        correctly when an id argument is provided during initialization.
        """
        base_instance = Base(42)
        self.assertEqual(base_instance.id, 42)
        my_base = Base(25)
        self.assertEqual(my_base.id, 25)

