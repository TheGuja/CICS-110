# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

A = input("Enter first string: ")
m = input("Enter first number: ")
B = input("Enter second string: ")
n = input("Enter second number: ")

minimum = int(min(m,n))
maximum = int(max(m,n))
remaining = maximum - minimum

print((A + B) * minimum, end='')

if int(m) == maximum:
    print((A) * remaining)
else:
    print((B) * remaining)
