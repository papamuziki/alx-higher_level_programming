#!/usr/bin/python3
"""
Module for function: append_write
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of text file(UTF8),
    and returns the number of chars added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
