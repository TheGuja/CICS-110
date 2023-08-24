# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import random

def get_guess():
    
    guess = input()
    guess = guess[:5].upper()
    return guess

def print_word(word):
    print(" ".join(word))

def exact_match_compare(soln, guess):

    output = ""
    index = 0

    for letter in guess:

        if letter == soln[index]:
            output += "🟢"
        else:
            output += "🔴"
        
        index += 1
    
    return output

def one_turn(soln):

    guess = get_guess()
    print_word(guess)
    print(exact_match_compare(soln, guess))

    if guess == soln:
        print("Congratulations")
        exit()

def make_solution():

    options = ["Which", "Their", "There", "Would", "Other", "These", "About", "First", "Could", "After"]
    return random.choice(options).upper()