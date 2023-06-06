#!/usr/bin/python3
"""
This module defines a function that divides a matrix's all elements
"""

def matrix_divided(matrix, div):
    """Divides a matrix"""
    import decimal
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(message)
    rLen = []
    rCount = 0
    for r in matrix:
        if type(r) is not list:
            raise TypeError(message)
        rLen.append(len(r))
        for element in r:
            if type(element) not in[int, float]:
                raise TypeError(message)
        rCount += 1
    if len(set(rLen)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    newMatrix = list(map(lambda r:
        list(map(lambda x: round(x/div, 2), r)), matrix))
    return newMatrix

