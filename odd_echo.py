# Odd echo problem

import sys

sample_input = """5
hello
i
am
an
echo"""

print([n for n in sample_input.splitlines() if n%2])