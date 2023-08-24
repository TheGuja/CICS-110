# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import math

class Frac:

    def __init__(self, sign, num, den):
        self.sign = sign
        self.num = int(num / (math.gcd(num, den)))
        self.den = int(den / (math.gcd(num, den)))

    def get_sign_num_den(self):
        return (self.sign, self.num, self.den) 
    
    def __str__(self):

        if self.num / self.den == 0:
            return "0"
        
        if self.sign == -1:
            return f"-{self.num}/{self.den}"
        
        return f"{self.num}/{self.den}"
    
    def __neg__(self):
        return Frac(-self.sign, self.num, self.den)
    
    def __add__(self, other):
        lcm = int(math.lcm(self.den, other.den))
        first_numerator = self.sign * self.num
        second_numerator = other.sign * other.num
        final_numerator = (first_numerator * int(lcm / self.den)) + (second_numerator * int(lcm / other.den))

        if final_numerator < 0:
            final_numerator = abs(final_numerator)
            final_sign = -1
        else:
            final_sign = 1

        return Frac(final_sign, final_numerator, lcm)
    
    def __sub__(self, other):
        return Frac(self.sign, self.num, self.den) + (-Frac(other.sign, other.num, other.den))
    
    def __mul__(self, other):
        new_numerator = self.num * other.num
        new_denominator = self.den * other.den
        new_sign = self.sign * other.sign

        return Frac(new_sign, new_numerator, new_denominator)
    
    def __truediv__(self, other):
        return Frac(self.sign, self.num, self.den) * Frac(other.sign, other.den, other.num)