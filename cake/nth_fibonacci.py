def fib(n):
    # Compute the nth Fibonacci number

    if n < 1:
        return 0
    elif n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


print(fib(2))
