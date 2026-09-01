#!/usr/bin/env python3

def pow(a, b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    p = 1
    for i in range(abs(b)):
        p = p*a

    if b < 0:
        return 1 / p

    return p


if __name__ == '__main__':
    print(pow(10, -2))
