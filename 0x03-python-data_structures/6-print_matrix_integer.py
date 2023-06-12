#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or len(matrix) == 0:
        print()
        return None
    if len(matrix) == 1 or len(matrix[0]) == 0:
        print()
        return None
    for row in matrix:
        for item in row:
            print("{:d}".format(item),end="") 
