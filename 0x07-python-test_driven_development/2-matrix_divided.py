#!/usr/bin/python3
"""This module divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """returns each element of matrix divided by div"""

    #each element in matrix should be int or float
    #matrix must be list of list

    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    for elm in matrix:
        if type(elm) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        for x in elm:
            if type(x) is not int and type(x) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    #same row size in matrix
    for elm in matrix:
        if len(elm) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    #div must be int or float
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    #div can't be zero
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return ([list(map(lambda x: round(x / div, 2), elm)) for elm in matrix])
