#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len_rows = len(matrix)
    for i in range(len_rows):
        len_colums = len(matrix[i])
        for j in range(len_colums):
            separ = " "
            if j == len_colums - 1:
                separ = "\n"
            print("{:d}".format(matrix[i][j]), end=separ)
