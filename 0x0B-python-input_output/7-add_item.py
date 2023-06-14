#!/usr/bin/python3

import json
import sys

"""
A script that adds all arguments to a Python list,
and then save them to a file
"""


save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file

try:
    py_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    py_list = []
for ar in sys.argv[0]:
    if ar is sys.argv[0]:
        continue
    py_list.append(ar)
    save_to_json_file(py_list, "add_item.json")
