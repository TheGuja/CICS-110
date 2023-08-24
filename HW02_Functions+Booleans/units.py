# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

def ounces_to_drams(ounces:float) -> float:
    return ounces * 8

def drams_to_ounces(drams:float) -> float:
    return drams / 8

def quarts_to_ounces(quarts:float) -> float:
    return quarts * 32

def ounces_to_quarts(ounces:float) -> float:
    return ounces / 32

def gallons_to_quarts(gallons:float) -> float:
    return gallons * 4

def quarts_to_gallons(quarts:float) -> float:
    return quarts / 4

def gallons_to_drams(gallons:float) -> float:
    quarts = gallons_to_quarts(gallons)
    ounces = quarts_to_ounces(quarts)
    drams = ounces_to_drams(ounces)
    
    return drams

def drams_to_gallons(drams:float) -> float:
    ounces = drams_to_ounces(drams)
    quarts = ounces_to_quarts(ounces)
    gallons = quarts_to_gallons(quarts)

    return gallons
