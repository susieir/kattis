# Oddities problem

# Import packages
import sys

# Input
sample_input = """3
10
9
-5"""

# Functions
def is_odd(input_num):
    """Checks if number is odd"""
    if input_num % 2 == 0:
        return(f"{input_num} is even")
    else:
        return(f"{input_num} is odd")

def read_num(input_str):
    """Reads and returns list of numbers from input string"""
    return [int(n) for n in input_str.splitlines()][1:]

def main(input_str):
    """Function to read string and return list of
    whether input numbers are odd or even"""
    return "\n".join([is_odd(i) for i in read_num(input_str)])

print(main(sys.stdin.read()))