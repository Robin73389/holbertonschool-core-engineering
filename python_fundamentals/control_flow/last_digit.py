#!/usr/bin/env python3

number = __import__('random').randint(-10000, 10000)

n = abs(number) % 10

if number < 0:
    n = -n
if n >= 5:
    print(f"Last digit of {number} is {n} and is greater than 5")
if n == 0:
    print(f"Last digit of {number} is {n} and is 0")
if n < 6 and n != 0:
    print(f"Last digit of {number} is {n} and is less than 6 and not 0")