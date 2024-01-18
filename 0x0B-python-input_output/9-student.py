#!/usr/bin/python3

"""
Student class module

Public instance attributes:\n
first_name\n
last_name\n

"""


class Student:
    """Class that defines a student."""
    def __init__(self, first_name, last_name, age):
        """Initialize the class objects."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve dictionary representation of student."""

        return self.__dict__

