#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    """_summary_

    Args:
        matrix (list, optional): _description_. Defaults to [[]].
    """
    for i in matrix:
        for c in i:
            if c != i[-1]:
                print("{:d}".format(c), end=' ')
            else:
                print("{:d}".format(c), end='')
        print()
