# Triangle problem

# Import packages
import sys

# Function


def triangle_area(input_str):
    """A function to calculate the area of a triangle from a string"""
    # Store base and height
    b_h = [int(n) for n in input_str.split(" ")]
    # Calculate area
    return b_h[0] * b_h[1] * 0.5

print(triangle_area(sys.stdin.read()))