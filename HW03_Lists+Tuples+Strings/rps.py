# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

def get_input():
    rps = input("Rock, Paper, Scissors? ")
    return rps.lower()

def p1_wins(p1:str, p2:str):
    if (p1.lower() == "rock" and p2.lower() == "scissors"):
        return True
    elif(p1.lower() == "scissors" and p2.lower() == "paper"):
        return True
    elif(p1.lower() == "paper" and p2.lower() == "rock"):
        return True
    else:
        return False

def p2_wins(p1: str, p2:str):
    if (p2.lower() == "rock" and p1.lower() == "scissors"):
        return True
    elif(p2.lower() == "scissors" and p1.lower() == "paper"):
        return True
    elif(p2.lower() == "paper" and p1.lower() == "rock"):
        return True
    else:
        return False

def tie(p1:str, p2:str):
    return p1.lower() == p2.lower()