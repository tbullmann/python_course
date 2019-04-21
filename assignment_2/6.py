"""
Result for 4)
Reuse function for Euclidean from 3)
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


def length(input_path):
    """
    Computes length of path by calculating the distance
    between the last two points and then dropping the last
    point until the path does not contain any pair of points.
    :param input_path: list of points as tuples of coordinates
    :return: length of path as the sum of Euclidean distances
    """
    result = 0
    path = input_path.copy()   # We have to copy because pop uses up the path
    while len(path) >= 2:
        result = result + distance(path[-2], path[-1])
        path.pop()
    return result


def length_2(path):
    """
    Computes length of path by calculating the distance between adjacent points.
    :param path: list of points as tuples of coordinates
    :return: length of path as the sum of Euclidean distances
    """
    result = 0
    for index in range(1, len(path)):
        result = result + distance(path[index-1], path[index])
    return result


a = (1, 1)
b = (4, 6)
c = (11, 2)
d = (23, 13)
path = [a, b, c, d]

print('Length of the path', path, 'is', length(path))
print('Length of the path', path, 'is', length_2(path), 'using another implementation')
