# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

def is_palindrome(s:str):
    palindrome = s[::-1]
    return s == palindrome

def is_anagram(s:str, t:str):
    sorted_s = sorted(s.lower())
    sorted_t = sorted(t.lower())

    return sorted_s == sorted_t
    

def same_word(s:str, t:str):
    return s.lower() == t.lower()

