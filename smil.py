# Problem - SMIL (https://open.kattis.com/problems/smil)

# Import packages
import sys

# Sample input
sample_input = ":-):);-):)"

# Smile list
smile_set = (":)",";)",":-)",";-)")

# Functions
def main(input_str):
    """"""
    output_str = ""
    for i in range(len(input_str)):
        if input_str[i:i+2] in smile_set:
            output_str+=f"{i} \n"
        elif input_str[i:i+3] in smile_set:
            output_str+=f"{i} \n"
    return output_str

print(main(sys.stdin.read()))
