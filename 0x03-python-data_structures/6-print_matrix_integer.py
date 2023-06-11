#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for x in matrix:
            print("\t".join(map(str, x)))
