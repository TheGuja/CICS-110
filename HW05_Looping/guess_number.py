# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import random

def choose_solution(min, max):
    return random.choice(range(min, max + 1))

def get_legal_guess(min, max):
    
    while True:
        num = int(input(f"Please enter a number beteween {min} and {max}: "))

        if (min <= num <= max):
            return num
        
        print(f"Guess was not between {min} and {max}")
        
def compare(solution, guess):

    if guess > solution:
        print("Too High")
        return False
    elif guess < solution:
        print("Too Low")
        return False
    else:
        print("That's It!")
        return True
    
def play_game(min, max, guess_limit):
    
    solution = choose_solution(min, max)
    guesses = 0

    while guesses < guess_limit:

        guess = get_legal_guess(min, max)

        if compare(solution, guess):
            break

        guesses += 1

    else:
        print(f"Out of guesses, answer was: {solution}") 
    
