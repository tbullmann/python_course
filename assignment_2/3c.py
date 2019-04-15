"""
Result for 3c)
Check the naive implementation of the geometric mean using the product:
For a sample of 1000 numbers it returns infinite as a result!
Below there is a better implementation using log and sum instead.
"""
from random import random

n = int(input('How many numbers do you want? '))

numbers = []                           # Start with an empty list
while len(numbers) < n:                # Repeat until list is full
    new_random_number = 100*random()   # Create new random float
    numbers.append(new_random_number)  # and append list

print('Here are your random numbers from the interval [0, 100]')
print(numbers)


from math import log, exp

def geometric_mean_naive(sample):
    """
    This is not a good implementation because for large sample the production become
    very large and for a sample of 1000 numbers it returns infinite as a result!
    :param sample: list of numbera
    :return: geometric mean
    """
    length = len(sample)
    product = 1
    for number in sample:
        product = product * number
    result = product ** (1/length)
    return result


print('Their geometric mean is', geometric_mean_naive(numbers))


def geometric_mean(sample):
    """
    This is a better implementation because it only adds.
    :param sample: list of numbera
    :return: geometric mean
    """
    length = len(sample)
    sum_of_logs = 0
    for number in sample:
        sum_of_logs = sum_of_logs + log(number)
    result = exp(sum_of_logs / length)
    return result


print('Their geometric mean is', geometric_mean(numbers))
