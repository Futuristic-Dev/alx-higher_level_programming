#!/usr/bin/python3

"""
Create a class Retangle that defines a rectangle by everything from\n
Module 2-recatngle.

Expanding that to include\n
printing out a rectangle with # character using print() and str()\n
and using __repr__ to print out the given name of the class\n
along with height and the width values.
"""

class Rectangle:
    """
    Instantiating variables of the width and the height

    Arguments of the class:
        width(int)
        height(int)
    """

    def __init__(self, width=0, height=0):

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("width must be an integer")

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
        based on valid width and height.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculate the perimeter of rectangle\n
        based on valid width and height.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print a rectangle with the # character."""
        if  self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""

        for r in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """
        String representation of the rectangle\n
        to recreate new instance.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

