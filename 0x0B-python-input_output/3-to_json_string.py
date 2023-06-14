#!/usr/bin/python3
"""
Module for function: to_json_string
"""

import json


def to_json_string(my_obj):
    """
    function returns the JSON representation of an object(string)
    """
    return json.dumps(my_obj)
