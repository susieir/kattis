# R2 problem

# Import packages
import sys

# Sample input
sample_input = """11 15"""

# Functions
def calc_r2(r1, mean):
    """Calculates input 2 using input 1 and mean"""
    return ((mean * 2) - r1)

def read_inputs(input_str):
    """Reads r1 and mean from string"""
    r1, mean = [int(i) for i in input_str.split(" ")]
    return r1, mean

def main(input_str):
    r1, mean = read_inputs(input_str)
    return calc_r2(r1, mean)

print(main(sys.stdin.read()))