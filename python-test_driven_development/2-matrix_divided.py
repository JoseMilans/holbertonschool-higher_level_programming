#!/usr/bin/python3
"""
This module contains a function that divides all elements
of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by div.
    Args:
        matrix: List of lists of integers/floats.
        div: Number (int/float) different from 0
        by which to divide each element of the matrix.
    Returns:
        New matrix with the result of the division rounded to 2 decimal places.
    Raises:
        TypeError: If matrix isn't a list of lists of ints/floats,
                   if each row of the matrix is not of the same size, or
                   if div is not a number.
    ZeroDivisionError: If div is 0.
    """

    mtrx_err = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(matrix, list):
        raise TypeError(mtrx_err)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(mtrx_err)
    for row in matrix:
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError(mtrx_err)
    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(elem / div, 2) for elem in row] for row in matrix]
