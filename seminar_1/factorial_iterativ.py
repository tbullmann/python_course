def factorial(n):
    """
    This computes n! by iteration of all factors and multiplying them.
    Print statements are just for demonstrating how it works.
    :param n: a number
    :return: factorial of n
    """
    factors = range(1, n+1)
    print('Factors are', list(factors))    # Print the iterator over factors as a list
    result = 1
    for factor in factors:
        print('Intermediate result =', result)
        print(' Multiply with factor', factor)
        result = result * factor
    return result


print('Final result for 5! =', factorial(5))
