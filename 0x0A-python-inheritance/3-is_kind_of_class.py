#!/usr/bin/python3

"""
Create a function that returns TRUE if the object is an instance of.

Or if the object is an inheritance of a class that inherited.
From the specified class; otherwise FALSE.
"""


def is_kind_of_class(obj, a_class):
    """Validate if the object is instance of a class."""
    if isinstance(obj, a_class):
        return (True)
    return (False)
