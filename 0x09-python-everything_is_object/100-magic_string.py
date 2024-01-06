#!/usr/bin/python3

"""Locked class module."""



class LockedClass:
    """
    Prevents user from dynamically creating any new instances.

    Instance attributes, except if new attribute is called.
    `first_name`
    """
    __slots__ = ('first_name')
    pass
