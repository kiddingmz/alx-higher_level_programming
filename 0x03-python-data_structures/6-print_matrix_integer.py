#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix[0]:
        len_rows = len(matrix)
        len_colums = len(matrix[0])
        for i in range(len_rows):
            for j in range(len_colums):
                separ = " "
                if j == len_colums - 1:
                    separ = "\n"
                print("{:d}".format(matrix[i][j]), end=separ)
