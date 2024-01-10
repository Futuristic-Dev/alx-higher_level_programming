#!/usr/bin/python3

"""Student class module."""


class Student:
    """Class that defines a Student."""
    def __init__(self, first_name, last_name, age):
        """
        Initialized the class objects

        Args:
            first_name, last_name, age):
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self. attrs=None):
        """Retrieve dict representation of student instance."""
        if attrs is None:
            return self.__dict__
        if not isinstance(attrs, list):
            return self.__dict__
        if not (isinstance(attrs[elements], str) for elements in attrs):
            return self.__dict__
        return {key:value for key, value in self.__dict__.items()
                if key in attrs}
