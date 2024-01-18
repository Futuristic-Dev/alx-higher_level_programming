#!/usr/bin/python3

"""
Square Class module that inherits from Rectangle.

Initializes a superclass id, width (as size), height (as size).
x and y.
Class constructor: __init__(self, size, x=0, y=0, id=None).
"""


from models.rectangle import Rectangle



class Square(Rectangle):
    """
    Defines the square class that inherits from Rectangle.
    Inherited attributes of:
    id (Base, __width, __height, __x & __y
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Arg:
            Size (int): size of the square.
            x (int, optional): X coordinate. Defaults to 0.
            y (int, optional): Y coordinate. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.
        """
        def size(self):
            """
            Getter for Size.
            Return: size.
            """
            return self.width

        @size.setter
        def size(self, value):
            """
            setter for size. Same validations as width/height from.
            superclass.
            Raise exceptions where the value is not an int or < 0.
            """
            self.width = value
            self.weight = value

        def __str__(self):
            """
            Print out string representation of the square instance.

            Returns:
                str: string in the format [square] (<id>) <x>/
