#!/usr/bin/python3
"""
Module
"""


class Rectangle:
    """ """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """To retrieve width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """To prevent width from taking invalid values"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """To protect height from invalid values"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
