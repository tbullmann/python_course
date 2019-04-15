"""
Result for 3a)
"""
from random import random

n = int(input('How many numbers do you want? '))

numbers = []                           # Start with an empty list
while len(numbers) < n:                # Repeat until list is full
    new_random_number = 100*random()   # Create new random float
    numbers.append(new_random_number)  # and append list

print('Here are your random numbers from the interval [0, 100]')
print(numbers)