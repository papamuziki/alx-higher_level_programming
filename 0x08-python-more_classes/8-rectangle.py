#!/usr/bin/python3
"""
Module
"""

class Rectangle:
    """
    Defines class rectangle
    """

    number_of_instances = 0
    print_simple = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __init__(self, width=0, height=0):
        """
        Attribs
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ """
        return self.__width

    @width.setter
    def width(self, value):
        """Protecting width from accepting invalid values"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of the rect"""
        return self.height * self.width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(sefl):
        """ """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                    for r in range(self.__height))
        return string

    def __repr__(self):
        """ """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
