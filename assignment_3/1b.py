"""
Result for 1b)
Now with user input.
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


A = []
print('Input matrix element by element:')
for row_index in [1, 2, 3]:
    row = []
    for column_index in [1, 2, 3]:
        element_name = 'a['+str(row_index)+','+str(column_index)+']='
        element = float(input(element_name))
        row.append(element)
    A.append(row)

print('The matrix:')
for row in A:
    print(*row)
print('has the determinant', det(A))
