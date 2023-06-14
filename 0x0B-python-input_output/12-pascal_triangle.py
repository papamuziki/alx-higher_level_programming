#!/usr/bin/python3
"""
function: pascal_triangle
"""


def pascal_triangle(n):
    """
    a function that returns a list of lists
    of integers representing the pascals triangle
    """
    if n <= 0:
        return []

    tr = [[1]]
    while len(tr) != n:
        t = tr[-1]
        temp = [1]
        for r in range(len(t) - 1):
            temp.append(t[r] + t[r + 1])
        temp.append(1)
        tr.append(temp)
    return (tr)
