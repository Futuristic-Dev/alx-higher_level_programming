#!/usr/bin/python3

"""
Write a class that defines a rectangle by, Private instance attribute.

Property - width and height.
Where width - def width(self).
Property setter - def width(self, value):
Where height - def height(self):
    height - def height(self, value):
Print a rectangle with # using print() and str().
"""


class Rectangle:
    """
    Instantiating variables of width and height 

    Arguments of the class:
        width(int)
        height(int)
    Dazzit, Dazzall.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self, value):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("width must be a integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculate the area of rectangle\n
        based on valid width and height provided.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculate the perimeter of rectangle.

        Based on width and height given.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print out a rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""

        for r in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str[:-1]




