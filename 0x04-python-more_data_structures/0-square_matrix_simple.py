#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map((lamba x: x * x), elm)) for elm in matrix]
