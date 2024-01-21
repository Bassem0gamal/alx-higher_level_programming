#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    #a function that computes the square value of all integers of a matrix

    new_matrix = []
    for i in matrix:
        result = list(map(lambada x: x**2, i))
        new_matrix.append(result)

        return new_matrix
