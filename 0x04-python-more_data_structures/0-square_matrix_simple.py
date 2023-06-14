#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in range(len(matrix)):
        new_row = list(map(lambda x: x ** 2, matrix[x]))
        new_matrix.append(new_row)
        return new_matrix
    print("{}".format(new_matrix)) 
