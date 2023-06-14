#!/usr/bin/python3
"""
class: Student
"""


class Student:
    """
    class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary rep of a student instance
        """
        if attrs is None:
            return self.__dict__
        new_dictionary = {}
        for r in attrs:
            try:
                new_dictionary[r] = self.__dict__[r]
            except FileNotFoundError:
                pass
            return new_dictionary

    def reload_from_json(self, json):
        """
        replaces all attribs
        """
        for k in json:
            try:
                setattr(self, k, json[k])
            except FileNotFoundError:
                pass

