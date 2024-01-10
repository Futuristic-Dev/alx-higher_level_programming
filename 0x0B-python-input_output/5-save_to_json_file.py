#!/usr/bin/python3

"""
Module to write an object into a text file using JSON.\n

Prototype: def save_to_json_file(my_obj, filename):
"""


def save_to_json_file(my_obj, filename):
    """
    Function to write an object to textfile.

    Args:
        my_obj: object to write
        filename: textfile to be written to.
    """
    import json

    with open(filename, 'w') as myFile:
        new_files = myFile.write(json.dumps(my_obj))
        return new_files
