#!/usr/bin/python3
"""
class: Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits class rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        str_sq = "[Square]"
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_sq + str_id + str_xy + str_wh

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        str_rect = "[Square]"
        str_id = "({})".format(self.id)
        str_xy = "{}/{}".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_rect + str_id + str_xy + str_size
