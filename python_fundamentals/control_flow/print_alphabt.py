#!/usr/bin/env python3

N = 26
res = ""

for i in range(N):
    if i != 4 and i != 16:
        res += chr(97 + i)

print("{}".format(res))
