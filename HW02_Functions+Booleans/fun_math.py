# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import math

def cullen(n:int) -> int:
    return n * 2**n + 1

def woodall(n:int) -> int:
    return n * 2**n - 1

def fermat(n:int) -> int:
    return 2**2**n + 1

def divides_evenly(dividend:int, divisor:int) -> bool:
    return dividend % divisor == 0

def is_square(n:int) -> bool:
    square_root = int(math.sqrt(n))
    return pow(square_root, 2) == n