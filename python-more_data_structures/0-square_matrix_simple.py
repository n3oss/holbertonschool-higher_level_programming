#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    y = []
    for x in matrix:
        t = []
        for j in x:
            t.append(j**2)
        y.append(t)
    return y
