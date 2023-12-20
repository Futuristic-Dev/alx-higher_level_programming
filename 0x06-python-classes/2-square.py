#!/usr/bin/python3

"""Create a class that defines a square."""
""" Private instance attribute, size."""


class Square:
    """Created a class Square."""

    def __init__(self, size=0):
        """Initialize the object, size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
