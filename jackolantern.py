# Jack 'O Lantern problem

def sep_and_multiply(int_string):
    """A function to return a list of integers from whitespace separate string"""
    return [int(i) for i in int_string.split(" ")]

def multiply_list(int_list):
    "A function to multiple a list of integers"
    t = 0
    multiple = 0
    for i in int_list:
        if t == 0:
            multiple = i
            t += 1
        else:
            multiple *= i
            t+=1
    return multiple

def main(int_string):
    "Separates a list of integers and multiplies"
    return multiply_list(sep_and_multiply(int_string))

import sys
input = sys.stdin.read()
print(main(input))