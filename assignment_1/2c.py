"""
Result for 2c)
This list of numbers looks interesting too :-)
"""
from math import sqrt, pi, e


def f(x):
    return sqrt(2*pi*x) * (x/e) ** x


numbers = [10, 15, 20]

for n in numbers:
    print('f(', n, ') =', f(n))
