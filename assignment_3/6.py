"""
Result for 6)
Recursive implementation for the calculation of binomial coefficients.
Also print Pascal's triangle nicely, although not requested
"""


def binom(n, k):
    """
    Calculates binomial coefficient (n over k)
    :param n: an integer
    :param k: an integer
    :return: binomial coefficient (n over k)
    """
    if k == 0:
        return 1
    elif n == k:
        return 1
    else:
        return binom(n - 1, k - 1) + binom(n - 1, k)


# Calculate binomial coefficients up to n = 10
max_n = 10

# Print Pascals triangle nicely, although not requested
for n in range(0, max_n):
    string = ""
    for k in range(0, n+1):
        string += str(binom(n, k)) + "   "  # One row of space delimited values
    print("{: ^80s}".format(string))        # Centered within 80 columns of the terminal

