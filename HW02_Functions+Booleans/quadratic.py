# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import math

def discriminant(a:float, b:float, c:float) -> float:
    return b**2 - (4 * a * c)

def has_real_root(a:float, b:float, c:float) -> bool:
    return discriminant(a, b, c) >= 0

def get_any_real_root(a:float, b:float, c:float) -> float:
    assert has_real_root(a, b, c)

    d = discriminant(a, b, c)
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    
    return x1