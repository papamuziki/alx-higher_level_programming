#!/usr/bin/python3
"""
Function: read_file
"""


def read_file(filename=""):
    """
    function that reads a text file and,
    prints it to stdout
    """
    with open(filename) as fn:
            for ln in fn:
                    print(ln, end="")
