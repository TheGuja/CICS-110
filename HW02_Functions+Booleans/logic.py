# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

def nand(a:bool, b:bool) -> bool:
    return not(a and b)

def implies(a:bool, b:bool) -> bool:
    return (not a) or b

def iff(a:bool, b:bool) -> bool:
    return ((a and b) or (not a and not b))

def xor(a:bool, b:bool) -> bool:
    return (a and (not b) or ((not a) and b))