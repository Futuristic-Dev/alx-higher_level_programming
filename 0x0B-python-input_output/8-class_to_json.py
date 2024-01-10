#!/usr/bin/python3

"""
Module to return the dictonary description with simple data\n
structure.
(list, dictionary, string, integer, boolean)

For JSON serialization of an object:\n
Prototype: def class_to_json(obj):\n
"""


def class_to_json(obj):
    """
    Class to json object.

    Return:
        The dict for JSON serialization of an object
    """
    return obj.__dict__
