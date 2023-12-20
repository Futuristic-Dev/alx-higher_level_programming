#!/usr/bin/python3

"""Create a  class Square that defines a square by private attribute."""
"""Public instance method, area(self)."""
"""Getter and Setter methods for size."""


class Square:
    """Instantiating variables self and size."""

    """Raising errors if conditions are not met."""

    def __init__(self, size=0):
        """Initialize private instance attribute, __size."""
        self.__size = size

    @property
    def size(self):
        """Return the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Validate if value is an integer."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculate the area of a square."""
        """Returns area."""
        return (self.__size ** 2)
