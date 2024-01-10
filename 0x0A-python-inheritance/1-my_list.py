#!/usr/bin/python3

"""
Create a class that inherits from list.

Prints list from public instance method: class MyList(list)\n
that prints the list.
"""


class MyList(list):
    "Prints list that is inherited from a class."
    def __init__(self):
        """Initialize for MyList."""
        super().__init__()

    def print_sorted(self):
        """
        Prints the list(sorted) in ascending order\n
        type(int).
        """
        print(sorted(self))
