#!/usr/bin/env python3


def islower(c):

    code = ord(c)

    if code >= 97 and code < 122:
        return True
    else:
        return False


if __name__ == "__main__":
    print(islower('a'))
    print(islower('A'))
    print(islower('3'))
