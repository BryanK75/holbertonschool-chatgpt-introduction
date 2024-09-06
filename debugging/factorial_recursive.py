#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the integer n.
    
    Raises:
    ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """
    Main function to execute the script. Reads an integer from command-line arguments,
    calculates its factorial, and prints the result.

    Expects:
    A single command-line argument which should be a non-negative integer.

    Raises:
    IndexError: If no command-line argument is provided.
    ValueError: If the provided argument is not a valid integer or is negative.
    """
    try:
        # Read the command-line argument
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
