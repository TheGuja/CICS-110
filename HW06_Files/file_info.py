# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import basic_io
import string

def get_info(fname):

    text = basic_io.read_string(fname)

    if text is not None:
        lines = len(text.splitlines())
        sentences = text.count(".")
    
        tokens = text.replace(".", "").replace("\n", " ").split()

        words = 0
        numbers = 0
        letters = 0
        digits = 0

        for word in tokens:
            if word[0] in string.ascii_letters:
                words += 1
                for char in word:
                    letters += 1
            else:
                numbers += 1
                for digit in word:
                    digits += 1

        dictionary = {
            "lines": lines,
            "sentences": sentences,
            "words": words,
            "numbers": numbers,
            "letters": letters,
            "digits": digits
        }

        return dictionary

def get_info_files(fname_list):

    info_dictionary = {}

    for name in fname_list:

        info = get_info(name)

        if info is not None:
            info_dictionary[name] = info

    return info_dictionary

def word_and_number_counts(fname):

    counts = {}
    text = basic_io.read_string(fname)

    if text is not None:

        tokens = text.replace(".", "").replace("\n", " ").split()

        for token in tokens:
            if token.lower() in counts:
                counts[token.lower()] += 1
            else:
                counts[token.lower()] = 1

        return counts

def word_and_number_counts_files(fname_list):

    counts_dictionary = {}

    for name in fname_list:

        counts = word_and_number_counts(name)

        if counts is not None:
            counts_dictionary[name] = counts

    return counts_dictionary

def letter_and_digit_counts(fname):

    counts = {}
    text = basic_io.read_string(fname)

    if text is not None:
        tokens = text.replace(".", "").replace("\n", " ").split()

        for token in tokens:
            for char in token:
                if char.lower() in counts:
                    counts[char.lower()] += 1
                else:
                    counts[char.lower()] = 1

        return counts

def letter_and_digit_counts_files(fname_list):

    counts_dictionary = {}
    
    for name in fname_list:

        counts = letter_and_digit_counts(name)

        if counts is not None:
            counts_dictionary[name] = counts

    return counts_dictionary