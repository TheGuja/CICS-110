# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

def print_1_to_n_while(n):
    
    for num in range(1, n + 1):
        print(num)

def print_1_to_n_for(n):

    for num in range(1, n + 1):
        print(num)

def echo_until_quit():

    while True:
        response = input("Please enter a word: ")

        if (response.lower() == "quit"):
            break

        print(response)

def multiple_words(s):

    words = s.split()

    if len(words) > 1:
        return True
    
    return False

def count_multiple_word_titles(titles):

    multiple_word_titles = 0
    
    for book in titles:
        if multiple_words(book):
            multiple_word_titles += 1

    return multiple_word_titles