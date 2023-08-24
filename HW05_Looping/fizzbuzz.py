# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID; 34231523

def fizzbuzz(n):

    if (n % 3 == 0) and (n % 5 == 0):
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return n
    
def first_n_fizzbuzz(n):

    list = []

    for num in range(1, n + 1):
        list.append(fizzbuzz(num))

    return list