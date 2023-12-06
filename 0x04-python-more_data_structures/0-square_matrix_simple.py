#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squre = []
    for i in matrix:
        squre.append([j ** 2 for j in i])
    return squre
