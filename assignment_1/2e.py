"""
Result for 2e)
Make sure to convert degree into radians
Reuse your factorial implementation
This function approximates sin() if the argument is small enough
"""
from math import sin, radians, pi


def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)


def f(x):
    return x/factorial(1) - x**3/factorial(3) + x**5/factorial(5)


angles = [radians(45), radians(90), 2 * pi]

for angle in angles:
    print('f(', angle, ') =', f(angle))
