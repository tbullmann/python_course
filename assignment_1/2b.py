"""
Result for 2b)
This can also be done iteratively.
"""


def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)


numbers = [10, 15, 20]

for n in numbers:
    print(n, '! =', factorial(n))
