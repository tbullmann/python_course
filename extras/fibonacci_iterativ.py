def fib(n):
    """
    This returns the n-th fibonacci number by iteratively expanding a list.
    Print statements are just for demonstrating how it works.
    :param n: a number
    :return: n-th fibonacci number
    """
    f = [0, 1]                    # Start with the first two fibonacci numbers
    while len(f) <= n:
        f.append(f[-2] + f[-1])
        print('Computed fibbonacci numbers are', f)
    return f[n]


print('Fibonacci number with index 10 is', fib(10))
