#!/usr/bin/python3

"""
Write a string into text file(UTF-8) and return a number of chars.

Prototype: def write_file(filename="", text=""):\n
Start with "with"
Keyword 'with' helps to exit a function safely, if the\n
the code crashes.
"""



def write_file(filename="", text=""):
    """
    Write a string into file and return number of characters.

    Args:
        filename: file to write to 
        text: content of the file
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        content = myFile.write(text)
        return (content)

