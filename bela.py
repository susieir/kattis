# Bela problem (https://open.kattis.com/problems/bela)

# Import packages
import sys

# Sample input
sample_input = """4 H
AH
KH
QH
JH
TH
9H
8H
7H
AS
KS
QS
JS
TS
9S
8S
7S"""

# Store score table
score_dict = {}
score_dict["A"] = [11, 11]
score_dict["K"] = [4, 4]
score_dict["Q"] = [3, 3]
score_dict["J"] = [20, 2]
score_dict["T"] = [10, 10]
score_dict["9"] = [14, 0]
score_dict["8"] = [0, 0]
score_dict["7"] = [0, 0]
#print(score_dict)


# Read input
def read_input(input_str):
    """
    A function that reads an input string to return
    number of hands
    value of dominant suit
    cards
    """
    # Initialise line counter and card list
    line_count = 0
    card_list = []
    # Loop through lines
    for line in input_str.splitlines():
        # Store number of hands and dominant suit
        if line_count == 0:
            num_hands, dom_suit = line.split(" ")
            line_count += 1
        else:
            card_list.append(line)
    return num_hands, dom_suit, card_list

# Calculate score
def calc_score(card_list, dom_suit, score_lookup):
    """A function that takes a dominant suit, list of cards and dictionary of scores
    and returns the total score"""
    # Initialise score counter
    score_counter = 0
    # Check card score
    #print(dom_suit)
    for card in card_list:
        #print(card)
        if card[1] == dom_suit:
            score_counter += score_lookup[card[0]][0]
            #print("Dominant - Score: ", score_lookup[card[0]][0])
        else:
            score_counter += score_lookup[card[0]][1]
            #print("Not dominant - Score: ", score_lookup[card[0]][1])
    return score_counter


def main(input_str, score_lookup):
    num_hands, dom_suit, card_list = read_input(input_str)
    return calc_score(card_list, dom_suit, score_lookup)


# Execute functions
print(main(sys.stdin.read(), score_dict))