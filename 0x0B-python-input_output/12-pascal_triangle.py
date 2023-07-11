#!/usr/bin/python3
"""Defines pascal's triangle as list of integers"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        row = [1]  # Each row starts with 1

        # Calculate the elements in the current row
        for j in range(1, i):
            element = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(element)

        row.append(1)  # Each row ends with 1
        triangle.append(row)

    return triangle
