#!/usr/bin/python3
"""
documentation: class instance checker
"""


def is_same_class(obj, a_class):
    """checks if the obj is exactly an instance of the specified class

    Return:
        True if the object is an instance, otherwise, False
    """

    return (type(obj) == a_class)
