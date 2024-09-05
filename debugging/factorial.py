#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using an iterative approach.

    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the integer n.
    
    Raises:
    ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid infinite loop
    return result

def main():
    """
    Main function to execute the script. Reads an integer from command-line arguments,
    calculates its factorial, and prints the result.

    Expects:
    A single command-line argument which should be a non-negative integer.

    Raises:
    IndexError: If no command-line argument is provided.
    ValueError: If the provided argument is not a valid non-negative integer.
    """
    try:
        # Check if a command-line argument is provided
        if len(sys.argv) != 2:
            raise IndexError("Please provide exactly one argument.")

        # Convert input to an integer
        n = int(sys.argv[1])

        # Calculate factorial
        f = factorial(n)

        # Print the result
        print(f)

    except IndexError:
        print("Error: Please provide a non-negative integer as an argument.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
