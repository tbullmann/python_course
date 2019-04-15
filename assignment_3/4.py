"""
Result for 4a,b,c)
"""

# Implementation for 4a
def fib(n):
    """
    This returns the n-th fibonacci number by recursion.
    :param n: a number
    :return: n-th fibonacci number
    """
    if n <= 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


# Implementation for 4b
def fibbonacci_numbers_recursive(max_index):
    """
    This returns a list with the first n fibonacci numbers computed by iteratively expanding a list.
    :param max_index: index of largest fibonacci numbers
    :return: list of fibonacci numbers
    """
    f = []  # Start with the first two fibonacci numbers
    for n in range(0, max_index + 1):
        f.append(fib(n))
    return f


# Implementation for 4c
def fibbonacci_numbers_iterative(max_index):
    """
    This returns a list with the first n fibonacci numbers computed by iteratively expanding a list.
    :param max_index: index of largest fibonacci numbers
    :return: list of fibonacci numbers
    """
    f = [0, 1]                    # Start with the first two fibonacci numbers
    while len(f) <= max_index:
        f.append(f[-2] + f[-1])
    return f


# Comparison
max_n = 45
print('First',max_n,'Fibonacci numbers:')
print('By recursion:')
print(fibbonacci_numbers_recursive(max_n))
print('By iteration:')
print(fibbonacci_numbers_iterative(max_n))
