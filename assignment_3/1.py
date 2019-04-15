"""
Result for 1)
Implementation of Sarrus rule.
"""


def det(matrix):
    """
    Computes the determinant for a 3 x 3 matrix
    :param A: List of rows, which are a list of numbers
    :return: determinant value of A
    """
    (a, b, c), (d, e, f), (g, h, i) = matrix
    result = a * e * i + b* f * g + c * d * h - g * e * c - h * f * a - i * d * b
    return result


A = [[0, 1, 2],
     [3, 2, 1],
     [1, 1, 0]]

print('The matrix:')
for row in A:
    print(*row)
print('has the determinant', det(A))
