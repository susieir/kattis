# Homework problem - https://open.kattis.com/problems/heimavinna

# Import packages
import sys

# Sample input
sample_input = "3;5"
sample_input_hard = "1-3;5;7;10-13"


# Functions
def return_range(input_str):
    range_limits = [int(n) for n in input_str.split("-")]
    return max(range_limits) - min(range_limits) + 1

def return_count(input_str):
    return len(input_str.split(";"))


def main(input_str):
    """A function to read a mixed set of problems and return a count"""

    # Initiate problem counter and string placeholder
    prob_counter = 0
    string_placeholder = ""
    string_placeholder += input_str

    # Find first "-" or ";"
    next_hyphen = input_str.find("-")
    next_colon = input_str.find(";")

    # Loop until all characters have been processed
    while len(string_placeholder) > 0:
        # If no colons, use range function to calc remaining problems
        if next_colon == -1:
            prob_counter += return_range(string_placeholder)
            string_placeholder = ""
        # If no hyphens, use count function to calc remaining problems
        elif next_hyphen == -1:
            prob_counter += return_count(string_placeholder)
            string_placeholder = ""
        # If both hyphens and colons present
        else:
            # If next block uses a hyphen first
            if next_hyphen < next_colon:
                # Extract segment with hyphen
                segment = string_placeholder[:next_colon]
                # Calculate problems and add to counter
                prob_counter += return_range(segment)
                # Remove range from placeholder
                string_placeholder = string_placeholder[next_colon + 1:]
                # Recalculate next hyphen and next colon
                next_hyphen = string_placeholder.find("-")
                next_colon = string_placeholder.find(";")
            else:
                # Increment counter and remove from placeholder
                prob_counter += 1
                string_placeholder = string_placeholder[next_colon + 1:]
                # Recalculate next hyphen and next colon
                next_hyphen = string_placeholder.find("-")
                next_colon = string_placeholder.find(";")

    return prob_counter


#print(main(sample_input))
#print(main(sample_input_hard))
print(main(sys.stdin.read()))

