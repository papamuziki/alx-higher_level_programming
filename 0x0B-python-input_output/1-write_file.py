#!/usr/bin/python3
"""
Module for function: write_file
"""


def write_file(filename="", text=""):
    """
    function that write a string to a text file (UTF8)
    and returns the number of characters
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
