# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

class Sequence:

    def __init__(self, function):
        self.function = function

    def generate_sequence(self, n):
        if n == 0:
            return [self.function(0)]
        else:
            seq = self.generate_sequence(n - 1)
            seq.append(self.function(n))
            return seq
    
def factorial(n):
    fact = 0

    if n == 0:
        fact = 1
    else:
        fact = n * factorial(n - 1)

    return fact

def fibonacci(n):
    fibo = 0

    if n in {0, 1}:
        fibo = n 
    else:
        fibo = fibonacci(n - 1) + fibonacci(n - 2)

    return fibo

def tribonacci(n):
    tribo = 0

    if n == 0:
        tribo = 0
    elif n in {1, 2}:
        tribo = n - 1
    else:
        tribo = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

    return tribo

def lucas(n):

    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
    
def padovan(n):
    if n in {0, 1, 2}:
        return 1
    else:
        return padovan(n - 2) + padovan(n - 3)
    
def pell(n):
    if n in {0, 1}:
        return n
    else:
        return 2 * (pell(n - 1)) + pell(n - 2)
    
def jacobsthal(n):
    if n in {0, 1}:
        return n
    else:
        return jacobsthal(n - 1) + (2 * (jacobsthal(n - 2)))