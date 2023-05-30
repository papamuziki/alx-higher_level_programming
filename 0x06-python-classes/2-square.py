#!/usr/bin/python3
""" defines a square """
class Square:
    """ private instance attribute: size """
    def __init__(self, size=0):
        """
        Args:
            size: the square size
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

