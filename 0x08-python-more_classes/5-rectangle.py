#!/usr/bin/python3

"""
Create a class Rectangle that defines a rectangle by\n
everything from module 4-rectangle\n
and expanding that  to include:\n
Print a message if a Rectangle is deleted.
"""


class Rectangle:
    """
    Instantiating varables of width and height.

    Arguments of the class:\n
        width (int)
        height (int)
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

    @height.setter
    def height(self, value):
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("height msut be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle\n
        Based on valid width and height provided.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculate the perimeter of rectangle\n
        Based on valid width and height given.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height == 0)

    def __str__(self):
        """Print a rectangle with the "#" character."""
        if self.__width == 0or self.__height == 0:
            return ""

        rectangle_str = ""

        for r in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """
        String representation of rectangle\n
        to recreate new instance.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Recognize if a rectangle is being deleted\n
        and print message.
        """
        print("Bye rectangle..")
