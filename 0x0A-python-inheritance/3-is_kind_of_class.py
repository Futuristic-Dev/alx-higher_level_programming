#!/usr/bin/python3

"""Create a function that validates if an object is an instance of a class."""


def is_kind_of_class(obj, a_class):
    """Validate if the object is instance of a class."""
    if isinstance(obj, a_class):
        return (True)
    return (False)
