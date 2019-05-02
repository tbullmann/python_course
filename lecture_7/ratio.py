# Use from Assignment 3.5

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


class Ratio():
    def __init__(self, numerator, denominator):
        assert all([type(numerator) is int, type(denominator) is int, denominator != 0])
        if (denominator < 0):
            numerator = -numerator
            denominator = -denominator
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return str(self.numerator) + "/" + str(self.denominator)

    def __eq__(self, other):
        assert type(other) is Ratio
        return str(self) == str(other)

    def expand(self, factor):
        self.denominator *= factor
        self.numerator *= factor
        return self

    def reduce(self):
        lcd = euklid(self.numerator, self.denominator)
        self.numerator //= lcd
        self.denominator //= lcd
        return self

    def __add__(self, other):
        assert type(other) is Ratio
        if self.denominator == other.denominator:
            return Ratio(self.numerator + other.numerator, self.denominator)
        else:
            # lcd (m,n) * scm(m,n) = m * n  ==>  scm(m,n) = m * [ n / lcd (m,n) ]
            lcd = euklid(self.denominator, other.denominator)
            self_factor = other.denominator//lcd
            other_factor = self.denominator // lcd
            self.expand(self_factor)
            other.expand(other_factor)
            return Ratio(self.numerator + other.numerator, self.denominator)



