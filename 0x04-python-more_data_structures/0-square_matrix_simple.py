#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    size = len(matrix)
    new_matrix = []

    for x in range(size):
        row = []
        for z in range(size):
            row.append(matrix[x][z] ** 2)
        new_matrix.append(row)

    return new_matrix
