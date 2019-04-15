"""
Result for 3b)
"""
from random import random

n = int(input('How many numbers do you want? '))

numbers = []                           # Start with an empty list
while len(numbers) < n:                # Repeat until list is full
    new_random_number = 100*random()   # Create new random float
    numbers.append(new_random_number)  # and append list

print('Here are your random numbers from the interval [0, 100]')
print(numbers)


def mean(sample):
    return sum(sample) / len(sample)


print('Their mean is', mean(numbers))


def median(sample):
    """
    Computes the median of the sample.
    Print statements are only for showing how it works.
    :param sample: list of numbers
    :return: median of the sample
    """
    sample.sort()                       # sort the numbers in the sample
    if len(sample) % 2 == 0:            # The % operator is the modulo function
        print('Equal number of numbers in the sample:')
        print('Median is average of two numbers in the middle of the sorted sample')
        a = sample[len(sample)//2]      # The // operator is integer division..
        b = sample[len(sample)//2 + 1]  # ..without the fraction 0.5
        return mean([a, b])             # Using the implementation of the mean
    else:
        print('Equal number of numbers in the sample:')
        print('Median is just the number in the middle of the sorted sample')
        b = sample[len(sample)//2]
        return b


print('Their median is', median(numbers))
