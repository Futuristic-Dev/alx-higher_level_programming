#!/usr/bin/python3
"""Create a function that prints all integers of a list."""


def print_list_integer(my_list=[]):
    """Create function to print the integers."""
    for item in my_list:
        print("{:d}".format(item))
