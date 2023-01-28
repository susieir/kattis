import sys
def return_range(input_str):
    range_limits = [int(n) for n in input_str.split("-")]
    return max(range_limits) - min(range_limits) + 1
def return_count(input_str):
    return len(input_str.split(";"))
def main(input_str):
    prob_counter = 0
    string_placeholder = ""
    string_placeholder += input_str
    next_hyphen = input_str.find("-")
    next_colon = input_str.find(";")
    while len(string_placeholder) > 0:
        if next_colon == -1:
            prob_counter += return_range(string_placeholder)
            string_placeholder = ""
        elif next_hyphen == -1:
            prob_counter += return_count(string_placeholder)
            string_placeholder = ""
        else:
            if next_hyphen < next_colon:
                segment = string_placeholder[:next_colon]
                prob_counter += return_range(segment)
                string_placeholder = string_placeholder[next_colon + 1:]
                next_hyphen = string_placeholder.find("-")
                next_colon = string_placeholder.find(";")
            else:
                prob_counter += 1
                string_placeholder = string_placeholder[next_colon + 1:]
                next_hyphen = string_placeholder.find("-")
                next_colon = string_placeholder.find(";")
    return prob_counter
print(main(sys.stdin.read()))

