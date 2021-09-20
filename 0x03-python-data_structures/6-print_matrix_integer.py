#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for elm in matrix:
        for i in elm:
            print(" ".join("{:d}".format(i)))
