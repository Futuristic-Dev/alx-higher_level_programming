#!/usr/bin/python3

"""Write a function that returns the list of available attributes and\n
methods of an object."""


def lookup(obj):
    """Prints  all attributes and methods of an object as a list."""
    return dir(obj)
