# Problem - Arrangement - https://open.kattis.com/problems/upprodun

# Import packages
import sys

# Sample input
sample_input = """3
8"""

# Functions


def read_input(input_str):
    """
    Takes a string and returns
    n - number of rooms
    m - number of teams
    """
    n,m = input_str.splitlines()
    return int(n),int(m)

def allocate_rooms(n,m):
    """
    Takes n rooms and m teams and
    returns min number of teams per room
    and number of rooms with an additional team
    """
    # Calculate room allocations
    min_teams = m//n
    add_teams = m%n

    # Initialise counter and output string
    counter = 0
    output_str = ""

    # Loop through each room
    for i in range(n):
        if counter < add_teams:
            output_str+=f"{'*'*min_teams}*\n"
        else:
            output_str+=f"{'*'*min_teams}\n"
        counter += 1
    return output_str


def main(input_str):
    """
    Reads input and returns output
    """
    n,m = read_input(input_str)
    return allocate_rooms(n,m)


# Print answers
print(main(sys.stdin.read()))