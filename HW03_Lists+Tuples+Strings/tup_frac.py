# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import math

def simplify(frac:tuple):
    common_factor = math.gcd(frac[0], frac[1])
    simple = (int(frac[0] / common_factor), int(frac[1]/ common_factor))
    return simple

def make_fraction(top:int, bottom:int):
    common_factor = math.gcd(top, bottom)
    fraction = (int(top / common_factor), int(bottom / common_factor))
    return fraction

def add(frac1:tuple, frac2:tuple):
    lcm = math.lcm(frac1[1], frac2[1])
    first_numerator = frac1[0] * (lcm / frac1[1])
    second_numerator = frac2[0] * (lcm / frac2[1])
    final_numerator = first_numerator + second_numerator

    return simplify((int(final_numerator), int(lcm)))

def negate(frac:tuple):
    negation = (-frac[0], frac[1])
    return negation

def sub(frac1:tuple, frac2:tuple):
    return add(frac1, negate(frac2))

def mul(frac1:tuple, frac2:tuple):
    final_numerator = frac1[0] * frac2[0]
    final_denominator = frac1[1] * frac2[1]

    return simplify((final_numerator, final_denominator))

def inverse(frac:tuple):
    if (frac[0] < 0):
        return (-frac[1], abs(frac[0]))

    return (frac[1], frac[0])

def div(frac1:tuple, frac2:tuple):
    absolute_value_inverse = inverse(frac2)
    return mul((frac1), (absolute_value_inverse))

