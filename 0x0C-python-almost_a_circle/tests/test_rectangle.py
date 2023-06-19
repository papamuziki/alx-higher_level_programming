#!/usr/bin/pthon3
"""
unittest for class Rectangle
"""
import unittest
import json
import os
import sys
import io
from contextlib import redirect_stout
from models.base import Base
from models.rectangle import Rectangle


class Rectangle(unittest.test_case):
    def set_up():
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        Base.reset_nb()
        self.rectangle = Rectangle(1, 2, 1, 2)


    def input_test(self):
        with self.assertRaises(TypeError):
            rect = Rectangle()

        with self.assertRaises(TypeError):
            rect = Rectangle(1)

        with self.assertRaises(TypeError):
            rect = rectangle(1, 2, 3, 4, 5, 6, 7, 8)

        rect = Rectangle(4, 9, 1, 3)
        self.assertTrue(isinstance(rect, Base))
        self.assertFalse(isinstance(Rectangle, Base))
        self.assertTrue(issubclass(Rectangle, Base))
