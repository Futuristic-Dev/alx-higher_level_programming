#!/usr/bin/python3

"""Create a class BaseGeometry."""


class BaseGeometry:
    """Creates a clas that defines the geometry."""

    def area(self):
        """Create a method."""
        raise Exception("area() is not implemented")

    def integer_validation(self, name, value):
        """Validates a value as an integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
