#!/usr/bin/python3

"""
Function that adds two integers/float numbers.

Prototype: def add_integer(a, b=98):\
Returns an integer: the addition of a and b.
"""


def add_integer(a, b=98):
    """
    Addition function of two integers.


    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
        Default to 98.
    Raises:
        TypeError: If either "a" or "b" is not an integer or float.
    Returns:
        int: The addition of "a" and "b" as an integer.
    """
    if not isinstance(a, (int, float)):
        raise:
            TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise:
            TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return int(a) + int(b)
