#!/usr/bin/python3

"""
Module to add all arguments to a Python list\n
and save them to a file.\n

Use function save_to_json_file from 5-save_to_json_file.py
"""


import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_check = len(sys.argv)

try:
    my_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    my_list = []

for x in range(1, arg_check):
    my_list.append(sys.argv[x])

save_to_json_file(my_list, 'add_item.json')
