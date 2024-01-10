#!/usr/bin/python3

"""
Create a function that returns TRUE if the object is an instance of a class that inherited\n
from a specified class; otherwise FALSE.
"""


def inherits_from(obj, a_class):
    """Validates if an object is an insttance of a class inherited."""
    if not type(obj) == a_class and issubclass(type(obj), a_class):
        return (True)
    else:
        return (False)
