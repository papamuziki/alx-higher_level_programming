#!/usr/bin/python3
"""
This is a module that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name
"""


class LockedClass:
    """Class to prevent dynamic creation of new atrributes"""
    __slots__ = ['first_name']

    def __init__(self):
        """The __init__ method"""
        pass
