# Homework problem - https://open.kattis.com/problems/heimavinna

# Import packages
import sys

# Sample input
sample_input = "3;5"

# Functions

def return_range(input_str):
    range_limits = [int(n) for n in input_str.split("-")]
    return max(range_limits) - min(range_limits) + 1

def return_count(input_str):
    return len(input_str.split(";"))

def main(input_str):
    if input_str.find("-") == -1:
        return return_count(input_str)
    else:
        return return_range(input_str)


#print(main(sys.stdin.read()))


##############################

sample_input_hard = "1-3;5;7;10-13"

# Initiate problem counter and string placeholder
prob_counter = 0
string_placeholder = ""
string_placeholder += sample_input_hard

# Find first "-" or ";"
next_hyphen = sample_input_hard.find("-")
next_colon = sample_input_hard.find(";")

print("Next colon: ",next_colon)
print("Next hyphen: ",next_hyphen)

# If no colons, use range function to calc problems
if next_colon == -1:
    print("No colon")
    print(return_range(sample_input_hard))
    prob_counter+=return_range(sample_input_hard)
# If no hyphens, use count function to calc problems
elif next_hyphen == -1:
    print("No range")
    print(return_count(sample_input_hard))
# Otherwise
else:
    while string_placeholder.find("-") + string_placeholder.find(";") > -2:
        print("Mixed string")
        # If next block uses a hyphen first
        if next_hyphen < next_colon:
            print("Range next")
            # Calculate range for that segment
            segment = string_placeholder[:next_colon]
            print(segment)
            prob_counter+=return_range(segment)
            # Remove range from placeholder
            string_placeholder = string_placeholder[next_colon+1:]
            print("String remaining:", string_placeholder)
            # Recalculate next hyphen and next colon
            next_hyphen = string_placeholder.find("-")
            next_colon = string_placeholder.find(";")

        else:
            print("Individual problems next")
            # Calculate range for that segment
            segment = string_placeholder[:next_hyphen]
            print(segment)
            prob_counter += return_count(segment)
            # Remove range from placeholder
            string_placeholder = string_placeholder[next_hyphen + 1:]
            # Recalculate next hyphen and next colon
            next_hyphen = string_placeholder.find("-")
            next_colon = string_placeholder.find(";")

            print("String remaining:", string_placeholder)
print(prob_counter)
        # If either return a -1, go to return_range or return_count functions

    # Start with whichever occurs first ("-" or ";")

    # If "-" read from start to "-" and "-" to next ";" or "-" (whichever comes first)

        # Convert to range

    # If ";" read from start to ";"

    # Drop the characters that have been read

    # Start over
