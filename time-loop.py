# Stuck in a time loop

# Import packages
import sys


def time_loop(n_input):
    """A function that takes a number and counts from 1 to N with a string appended"""
    return '\n'.join([n for n in [str(i+1)+" Abracadabra" for i in range(int(n_input))]])

# Check
#print(time_loop("10"))
# Input
print(time_loop(sys.stdin.read()))