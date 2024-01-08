#!/usr/bin/python3

"""
Matrix Division module

The module takes in a list of lists matrix and divisor.
Contains method that diviides all the elements of a matrix\n
and returns new matrix
Requires same size lists of ints or float, and max two decimal places.
"""



def matrix_divided(matrix, div):
    """
    Return a new matrix with all values divided by `div`.

    Matrix must be a list of lists.
    Each sub-list must contain only integers or floats.
    Empty sub-lists are not allowed.
    Divisor must greater than 0 and must be an int or float.
    """
    matrixErrMsg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix:
        raise TypeError(matrixErrMsg)


