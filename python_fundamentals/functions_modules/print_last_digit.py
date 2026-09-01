#!/usr/bin/env python3

def print_last_digit(number):
    """_summary_

    Args:
        number (_type_): _description_

    Returns:
        _type_: _description_
    """
    last_digit = abs(number) % 10

    print(last_digit)
    return last_digit


if __name__ == '__main__':
    print_last_digit(98)
