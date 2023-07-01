#!/usr/bin/python3
"""
This is a  module for a function that adds two numbers
"""

def add_integer(a, b=98):
    """Adds 2 integers
    Args:
        a: first number
        b: second number
    Returns:
        Sum of the given 2 numbers
    Raises:
        TypeError: if a or b are not integers and or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
