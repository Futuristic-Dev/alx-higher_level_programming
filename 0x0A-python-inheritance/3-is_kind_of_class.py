#!/usr/bin/python3

"""
Create a function that returns TRUE if the object is an instance of, or if the object is an\n
inheritance of a class that inherited from the specified class; otherwise FALSE.
"""


def is_kind_of_class(obj, a_class):
    """Validate if the object is instance of a class."""
    return (isinstance(obj, a_class))
