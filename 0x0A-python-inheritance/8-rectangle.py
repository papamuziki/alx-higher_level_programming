#!/usr/bin/python3
"""
documentation: class BaseGeometry
"""


class BaseGeometry:
    """
    class with public instance methods
    """

    def area(self):
        """
        Raise exceptions
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from class BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiation of the rectangle instance

        Args:
            width (int) : the width of the rectangle
            height (int): the height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
