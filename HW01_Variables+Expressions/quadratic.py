# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

discriminant = b ** 2 - (4 * a * c)
first_root = (-b - (discriminant ** (1/2))) / (2 * a)
second_root  = (-b + (discriminant ** (1/2))) / (2 * a)

print(f"{a} * x^2 + {b} * x + {c} has roots:")
print(first_root)
print(second_root)