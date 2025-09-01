#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input number n.

    Raises:
        RecursionError: If n is too large for recursion depth.
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except (IndexError, ValueError):
        print("Usage: ./script.py <non-negative-integer>")

