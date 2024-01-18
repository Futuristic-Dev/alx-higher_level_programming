#!/usr/bin/python3

"""Create a class Square that defnes a square by."""
"""Private instance attribute, __size."""
"""Public instance method, area(self)."""
"""And return the current square area."""


class Square:
    """Initialise/instantiate the varibles self and size."""

    """Raising errors if conditons are not met."""

    def __init__(self, size=0):
        """Initilaise the private instance atttribute,__size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculate the area of a square."""
        """Return value of area."""
        return (self.__size ** 2)
