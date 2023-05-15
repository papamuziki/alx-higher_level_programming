#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix_length = len(matrix[0])
    for i in range(len(matrix)):
        for c in range(len(matrix[0])):
            if c < matrix_length - 1:
                print("{:d}".format(matrix[i][c]), end=" ")
            else:
                print("".format(matrix[i][c], end=" "))
        print()
