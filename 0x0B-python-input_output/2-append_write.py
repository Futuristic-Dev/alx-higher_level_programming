#!/usr/bin/python3

"""
Module that appends a string at the end of a text file(utf-8).

Return the number of chars added.
Prototype: def append_write(filename="", text=""):\n
"""


def append_write(filename="", text=""):
    """
    Append string to end of the text.

    Args:
        filename: where to write to
        text: content of the file
    """
    with open(filename, 'a', encoding="utf-8") as myFile:
        content = myFile.write(text)
        return (content)
