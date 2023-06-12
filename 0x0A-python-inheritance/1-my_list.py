#!/usr/bin/python3
"""
Module of class: MyList
"""


class MyList(list):
    """
    class MyList that inherits class list
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
