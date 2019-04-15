"""
Result for 2a)
This list of numbers looks interesting :-)
"""
from math import sqrt, floor


def f(x):
    a = sqrt(5)   # Compute some intermediate result
    result = 1/a * (((1+a)/2)**x - ((1-a)/2)**x)
    return floor(result)   # Discard fractional part


numbers = [1, 2, 3, 4, 5, 6, 7]

for n in numbers:
    print('f(', n, ') =', f(n))
