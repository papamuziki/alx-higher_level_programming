#!/usr/bin/python3
"""
Module for  a class, Rectangle.
"""


class Rectangle:
    """
    Defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize class
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """To retrieve the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """To protect width from receiving invalid values"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self._width = value

    @property
    def height(self):
        """To retrieve height"""

        return self.__height

    @height.setter
    def height(self, value):
        """To protect height from receiving invalid values"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
