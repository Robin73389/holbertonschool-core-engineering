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
    for i in range(b):
        p = p*a

    return p


if __name__ == '__main__':
    print(pow(2, 4))
