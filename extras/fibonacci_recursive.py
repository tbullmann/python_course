def fib(n):
    """
    This returns the n-th fibonacci number by recursion.
    Print statements are just for demonstrating how it works.
    :param n: a number
    :return: n-th fibonacci number
    """
    if n <= 1:
        print('By definition fib(', n, ') =', n)
        return n
    else:
        print('Computing fib(', n, ') = fib(', n - 2, ') + fib(', n - 1, ')')
        return fib(n - 2) + fib(n - 1)


print('Fibonacci number with index 10 is', fib(10))
