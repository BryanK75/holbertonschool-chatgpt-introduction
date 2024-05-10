#!/usr/bin/python3
import sys

# Get the number of command line arguments
num_args = len(sys.argv)

# Start from index 1 to skip the script name
for i in range(1, num_args):
    print(sys.argv[i])

