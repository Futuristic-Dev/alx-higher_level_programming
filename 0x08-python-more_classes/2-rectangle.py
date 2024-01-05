#!/usr/bin/python3

"""
Write a class Rectangle that defines a rectangle.

Private instance attribute, width;
Private instance attribute,height;
Methods getter and setters properties fot the width and height.
Raissing erors if valid coditions are not successful.
Public instance method  of area that  returns the area of the rectangle.
Public instance method of perimeter that returns the perimeter.
If width or height is 0, perimeter is 0.
"""


class Rectangle:
    """
    Instantiating variables of width and height.

    Arguments of class Rectangle:
        width (int)
        height (int)
    """

    def __init__(self, width=0, height=0):
        """Initialize private attributes."""
        self.__width = width
        self.__height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) is not int or isinstance(value, (float, bool)):
                raise TypeError("height must be an integer")

            if value < 0:
                raise ValueError("height must be >= 0")

            self.__height = value

            def area(self):
                """
                Calculate the area of the rectangle.
                
                Based on valid width and height given.
                """
                return (self.__width * self.__height)

            def perimeter(self):
                """
                Calculate the perimeter of the rectangle.

                Based on valid width and heights.
                """
                if self.__width == 0 or self.__height == 0:
                    return 0
                return 2 * (self.__width + self.__height)
