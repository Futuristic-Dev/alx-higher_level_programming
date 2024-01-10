#!/usr/bin/python3

"""
Module for based on `7-base_geometry.py`.

This creates a class rectangle.
"""



BaseGeometry = __import__('7-base_geometry').BaseGeometry)


class Rectangle(BaseGeometry):
    """
    Creates a class Rectangle that extends from\n
    BaseGeometry.
    """
    def __init__(self, width, height):
        """Initialise the props."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
