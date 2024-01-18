#!/usr/bin/python3
"""Create a function that prints all integers of a list."""


def element_at(my_list, idx):
    """Create a function to print out the index."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
