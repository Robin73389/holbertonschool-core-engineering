#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):

    taille = 0
    for i in range(x):

        try:
            print(my_list[i], end='')
            taille += 1

        except IndexError:
            break

    print()
    return taille
