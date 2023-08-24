# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import random

class MarbleBag():
    def __init__(self, red_marbles, green_marbles, blue_marbles):
        self.red_marbles = red_marbles
        self.green_marbles = green_marbles
        self.blue_marbles = blue_marbles

    def get_contents(self):
        return {
            "red": self.red_marbles,
            "green": self.green_marbles,
            "blue": self.blue_marbles
        }
    
    def take_marble(self):

        marbles = []

        if self.red_marbles != 0:
            marbles.append("red")
        if self.green_marbles != 0:
            marbles.append("green")
        if self.blue_marbles != 0:
            marbles.append("blue") 

        if len(marbles) > 0:
            chosen_marble = random.choice(marbles)

            if chosen_marble == "red":
                self.red_marbles -= 1
                return chosen_marble
            elif chosen_marble == "green":
                self.green_marbles -= 1
                return chosen_marble
            elif chosen_marble == "blue":
                self.blue_marbles -= 1
                return chosen_marble
            
        else:
            print("Bag is empty.")
            return None
        
    def add_marbles(self, add_red, add_green, add_blue):
        self.red_marbles += add_red
        self.green_marbles += add_green
        self.blue_marbles += add_blue

    def all_permutations(self):
        marbles = []
        final_set = set()

        if (self.red_marbles == 0) and (self.green_marbles == 0) and (self.blue_marbles == 0):
            return {()}
        
        for i in range(self.red_marbles):
            marbles.append("red")

        for i in range(self.green_marbles):
            marbles.append("green")

        for i in range(self.blue_marbles):
            marbles.append("blue")
        
        permutations = self.permutations_helper(marbles)

        for perm in permutations:
            current_perm = tuple(perm)
            final_set.add(current_perm)

        return final_set
    
    def permutations_helper(self, marbles):
        if len(marbles) == 0:
            return []
        if len(marbles) == 1:
            return [marbles]

        result = []
        for i in range(len(marbles)):
            rest = marbles[:i] + marbles[i + 1:]
            for marble in self.permutations_helper(rest):
                result.append([marbles[i]] + marble)
        return result
    
    def __str__(self):
        return f"The marble bag has {self.red_marbles} red, {self.green_marbles} green, and {self.green_marbles} blue marbles."