# Cold-puter science problem

# Import packages
import sys

# Import sample input
sample_input = """5
-14 -5 -39 -5 -7"""

# Read temperatures into list
def read_temps(input_str):
    """Reads second line of input string into list of values"""
    temps_count = sum([1 for i in [int(n) for n in input_str.splitlines()[1].split()] if i < 0])
    return temps_count

# Test output
#print(read_temps(sample_input))
# Actual output
print(read_temps(sys.stdin.read()))