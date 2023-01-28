# Carrots problem - https://open.kattis.com/problems/carrots

# Import packages
import sys

# Sample input
sample_input = """1 5
sovl problmz"""

# Functions

def extract_int(input_str):
    """A function to extract an integer"""
    return input_str.splitlines()[0].split(" ")[1]

#print(extract_int(sample_input))
print(extract_int(sys.stdin.read()))