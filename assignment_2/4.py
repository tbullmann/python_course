"""
Result for 4)
"""
from random import randint

x = randint(1, 100)
print ('I have a random number between 1 an 100.')

n = None   # Up till now there was no input from user

while n != x:
    n = int(input('What is your guess? '))
    if n == x:
        print('That is right!')
    elif n > x:
        print('That is too big.')
    else:
        print('That is too low.')
