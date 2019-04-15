"""
Result for 4)
Here we add a counter for the number of guesses to find the random number.
With the optimal strategy, within how many trials you would find the number?
"""
from random import randint

x = randint(1, 100)
print ('I have a random number between 1 an 100.')

n = None   # Up till now there was no input from user
trial = 1  # Start with first trial

while n != x:
    n = int(input('What is your guess? '))
    trial += 1    # Increase number of trial by 1
    if n == x:
        print('That is right!')
    elif n > x:
        print('That is too big.')
    else:
        print('That is too low.')

print('That took you', trial, 'trials.')
