#!/usr/bin/python3

"""
Using the UTF-8, read a text file.

Print to stdout.
Prototype: def read_file(filename=""):\n
You must use the 'with' statement
"""


def read_file(filename=""):
    """
    Open and read a UTF-8 file and print to stdout.

    Args:
        filename
    """
    with open(filename, encoding="UTF8") as myfile::
        text = myfile.read()
        print(text, end="")
