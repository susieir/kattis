# Odd echo problem

import sys

sample_input = """10
only
if
these
oddindexed
words
appear
are
you
correct
output"""


def main(input_str):
    """Returns odd words from input string"""
    output_iter = [n for i, n in enumerate(input_str.split("\n")) if i % 2]
    output_str = ""
    for n in output_iter:
        output_str+= n
        output_str+= "\n"
    return output_str

print(main(sys.stdin.read()))
#print(odd_echo(sample_input))
