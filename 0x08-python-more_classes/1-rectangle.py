#!/usr/bin/python3
"""
A module made up of class that defines rectangle
"""


class Rectangle:
    """A class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Method to initialize the instance
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Method that returns the value of the width
            Args:
                value: width
            """

            return self.__width

        @width.setter
        def width(self, value):
            """Method to define width
            Args:
                value: width
            raises:
                TypeError: width must be an integer
                ValueError: width must be >= 0
            """

            if not isinstance(self, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Method returning value of the height
            Args:
                height of the rectangle
            """

            return self.__height

        @height.setter
        def height(self, value):
            """Method defining height of the rectangle
            Args:
                value: height
            raises:
                TypeError: height must be an integer
                ValueError: height must be >= 0
            """

            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
