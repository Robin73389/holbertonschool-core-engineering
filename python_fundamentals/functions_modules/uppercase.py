#!/usr/bin/env python3


def uppercase(str):
    """_summary_

    Args:
        str (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = ""

    for i in str:

        if 'a' <= i <= 'z':
            result += chr(ord(i) - 32)
        else:
            result += i

    print("{}".format(result))


if __name__ == '__main__':
    uppercase("holberton")
