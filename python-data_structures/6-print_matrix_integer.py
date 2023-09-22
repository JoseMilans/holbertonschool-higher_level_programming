#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        x_len = len(x)
        for idx in range(x_len):
            y = x[idx]
            if idx == x_len - 1:
                print("{:d}".format(y), end="")
            else:
                print("{:d} ".format(y), end="")
        print()
