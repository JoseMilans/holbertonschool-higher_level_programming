#!/usr/bin/python3
"""
Module for creating Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Creates pascal's triangle of size n.
    Returns a list of lists representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j + 1])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
