# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

seconds = input("Enter a number of seconds: ")
days = int(seconds) // 86400

remainder_hour = int(seconds) % 86400
hours = remainder_hour // 3600

remainder_minutes = remainder_hour % 3600
minutes = remainder_minutes // 60

remainderSeconds = remainder_minutes % 60

print(f"{seconds} seconds can be broken up into:")
print(f"{days:.0f} days,")
print(f"{hours:.0f} hours,")
print(f"{minutes:.0f} minutes, and")
print(f"{remainderSeconds} seconds.")