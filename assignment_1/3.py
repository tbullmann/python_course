"""
Result for 3)
"""
from math import sqrt


def distance(x, y):
    """
    Computes the Euclidean distance between point A and B.
    :param x: first point as a tuple of two coordinates
    :param y: second point as a tuple of two coordinates
    :return: distance
    """
    # Remember tuples index starts from 0
    return sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)


x = (3, 5)
y = (7, 11)

print('Euclidean distance between', x, 'and', y, 'is', distance(x, y))
