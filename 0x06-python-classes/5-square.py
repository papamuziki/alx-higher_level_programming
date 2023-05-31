#!/usr/bin/python3
""" define class Square """

class Square:
    """ represent a square
    Attributes: 
        __size(int): size of a square side
    """
    def __init__(self, size=0):
        """
        initialize the square
        Args:
            size(int): square side size
        Returns:
            None
        """
        self.size = size

    def area(self):
        return (self.__size) ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for r in range(self.__size):
            print("".join(["#"for c in range(self.__size)]))
