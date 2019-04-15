def factorial(n):
    """
    This computes n! by recursion.
    Print statements are just for demonstrating how it works.
    :param n: a number
    :return: factorial of n
    """
    if n <= 1:
        print('By definition factorial(', n, ') = 1')
        return 1
    else:
        print('Computing factorial(', n, ') =', n, '* factorial(', n - 1, ')')
        return n * factorial(n - 1)


print('Final result for 5! =', factorial(5))
