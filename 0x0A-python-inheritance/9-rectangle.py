#!/usr/bin/python3

"""
Module based on 7-base_geometry.

This class creates a rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle extends from BaseFeometry(parent class)."""

    def __init__(self, width, height):
        """
        Initialize the objects of  the class.

        Arguments:
            width
            height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Return string of rectangle format."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
