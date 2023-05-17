#!/usr/bin/python3

# computes the square values of all integers 
# of a matrix

def square_matrix_simple(matrix=[]):
    newMatrix = []
    for r in range(len(matrix)):
        newMatrix.append([c ** 2 for c in matrix[r]])
    return newMatrix
