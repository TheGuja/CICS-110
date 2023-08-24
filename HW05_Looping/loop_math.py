# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import math

def is_prime(n):

    for num in range(2, math.ceil(math.sqrt(n + 1))):
        if n % num == 0:
            return False
        
    return True

def first_n_primes(n):

    primes = []
    current_num = 2

    while len(primes) < n:
        if is_prime(current_num):
            primes.append(current_num)
            current_num += 1
        else:
            current_num += 1

    return primes

def next_collatz_number(n):
    
    if n % 2 == 0:
        return int(n / 2)
    else:
        return (n * 3) + 1
    
def collatz_sequence(n):
    
    sequence = [n]
    
    while n != 1:
        n = next_collatz_number(n)
        sequence.append(n)
        
    return sequence

def first_n_collatz_sequences(n):

    seqeunces = []

    for sequence in range(1, n + 1):
        seqeunces.append(collatz_sequence(sequence))

    return seqeunces
