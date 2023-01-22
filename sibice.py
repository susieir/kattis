# Sibice problem - https://open.kattis.com/problems/sibice

# Import libraries
import sys

# Sample input
sample_input = """2 12 17
21
20"""

# Functions

def read_input(input_str):
    """A function that reads an input string and returns
    number of matches, dimensions of match box (W and H)
    and a list of match lengths"""

    # Initialise line counter and match length list
    line_count = 0
    match_list = []

    for l in input_str.splitlines():
        if line_count == 0:
            num_matches, box_w, box_h = l.split(" ")
            line_count+=1
        else:
            match_list.append(int(l))
    return  int(num_matches), int(box_w), int(box_h), match_list


def calc_diag(box_w, box_h):
    """Takes box dimensions to calculate hypotenuse (diagonal)"""
    return int(((box_w**2) + (box_h**2))**0.5)

def check_match(match_l, width, height):
    """A function that uses the width and height to check whether a match fits in the box"""
    box_diag = calc_diag(width, height)
    if match_l <= max(box_diag, width, height):
        return "DA"
    else:
        return "NE"

def main(input_str):
    """Function to produce answer"""
    # Read input into variables
    num_matches, box_w, box_h, match_list = read_input(input_str)

    # Create output string
    output_str = ""

    # Check matches
    for match in match_list:
        output_str+=check_match(match, box_w, box_h)
        output_str+="\n"

    return output_str


# Return answer
print(main(sys.stdin.read()))