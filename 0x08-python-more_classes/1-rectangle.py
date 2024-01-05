#!/usr/bin/python3

"""
Write a class Rectangle that defines a rectangle.

Private instance attribute width, has a property - def width(self).
Private instance attribute  height;
Methods getter and setter properties for the width and height.
"""


class Rectangle:
    """
    Instantiating variables of width and height.

    Arguments of the class:
        width (int)
        height (int)
    """

    def __init__(self, width=0, height=0):
        """Initialize private instance attribute."""
        self.height = height
        self.width = width

        @property
        def width(self):
            return self.__width

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) is not int or isinstance(value, (float, bool)):
                raise TypeError("height must be an integer")

            if vaue < 0:
                raise ValueError("height must be >= 0")

            self.__height = value
