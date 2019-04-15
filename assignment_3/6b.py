"""
Result for 6)
Iterative implementation for the calculation of binomial coefficients.
Also print Pascal's triangle nicely, although not requested
"""


def binomial_coefficients(max_n):
    """
    Calculates binomial coefficients (n over k)
    :param max_n: largest n
    :return: list of lists with binomial coefficients
    """
    binom = [[1], [1, 1]]          # start with the first two rows of the triangle
    while len(binom) <= max_n:
        n = len(binom[-1])         # length of last row
        new_row = [1, ]          # new row starts with 1
        for k in range(0, n-1):  # calculate coefficients by adding adjacent coefficients of the last row
            new_row.append(binom[-1][k] + binom[-1][k+1])
        new_row.append(1)        # new row ends with 1
        binom.append(new_row)      # append new row to the triangle
    return binom


# Calculate binomial coefficients up to n = 10
max_n = 10
binom = binomial_coefficients(max_n)

# Print Pascals triangle nicely, although not requested
for n in range(0, max_n):
    string = ""
    for k in range(0, n+1):
        string += str(binom[n][k]) + "   "  # One row of space delimited values
    print("{: ^80s}".format(string))        # Centered within 80 columns of the terminal

