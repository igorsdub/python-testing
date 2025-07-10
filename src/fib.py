def fib(n):
    if n == 0 or n == 1:
        return n
    elif n < 0 or not isinstance(n, int):
        return NotImplemented
    else:
        return fib(n - 1) + fib(n - 2)