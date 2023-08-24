# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

fahrenheit = input("Enter temperature in Fahrenheit: ")
celsius = (float(fahrenheit) - 32) * 5 / 9
kelvin = celsius + 273.15

print(f"{fahrenheit} degrees Fahrenheit is equivalent to: ")
print(f"{celsius} degrees Celsius")
print(f"{kelvin} degrees Kelvin")