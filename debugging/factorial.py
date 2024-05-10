#!/usr/bin/python3
import sys
import math
"""
factorial - calculate the factorial of a given number
@n: the number of which to calculate the factorial
Return: integer the factorial of the input number
"""

def factorial (n):
    if n < 0:
        raise ValueError("Factoril is not defined for negative numbers")
    elif n == 0:
        return (1)
    else:
        result = 1
        while n > 1:
            result *= n
            n -= 1
    return result
if len(sys.argv) != 2:
    print("Usage: python script.py <number>")
    sys.exit(1)

try:
    num = int (sys.argv[1])
except ValueError:
    print("Please provide a valid integer")
    sys.exit(1)
try:
    f = factorial(num)
    print(f)
except ValueError as e:
    print(e)
    sys.exit(1)
