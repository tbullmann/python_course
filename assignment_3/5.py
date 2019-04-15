"""
Result for 5)
"""


def euklid(a, b):
    """
    Implements Euklid's algorithm from pseudo-code.
    :param a: an integer
    :param b: an integer
    :return: largest common divisor of a and b
    """
    if b == 0:
        return a
    elif a == 0:
        return b
    elif a > b:
        return euklid(a - b, b)
    else:
        return euklid(a, b - a)


# Testing
print("Largest common divisor for two integers by Euklid's algorithm:")
print('1, 1 --> ', euklid(1, 1))
print('0, 1 --> ', euklid(0, 1))
print('3, 2 --> ', euklid(3, 2))
print('6, 8 --> ', euklid(6, 8))
