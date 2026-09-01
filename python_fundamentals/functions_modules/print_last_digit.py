#!/usr/bin/env python3

def print_last_digit(number):
    last_digit = abs(number) % 10

    return last_digit


if __name__ == '__main__':
    print(print_last_digit(-1024))
