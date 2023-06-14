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
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {r: getattr(self, r) for r in attrs if hasattr(self, r)}
        return self.__dict__
