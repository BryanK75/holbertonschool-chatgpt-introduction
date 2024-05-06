#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number recursively.

    Parameters:
    - n (int): The number for which the factorial is to be calculated.

    Returns:
    - int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Check if a command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: python3 filename.py <number>")
    sys.exit(1)

try:
    # Convert the command-line argument to an integer
    num = int(sys.argv[1])
    # Check if the number is non-negative
    if num < 0:
        raise ValueError("Number must be non-negative.")
except ValueError as e:
    print("Error:", e)
    sys.exit(1)

# Calculate the factorial
f = factorial(num)

# Print the result of the factorial calculation
print(f)

