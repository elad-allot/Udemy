def fib(n):
    if n in [0, 1]:
        return n
    return fib(n-1) + fib(n-2)


def fib_mem(n, memo=[0, 1]):
    if n in [0, 1]:
        return n
    elif len(memo) > n:
        return memo[n]
    else:
        memo.append(fib_mem(n-1) + fib_mem(n-2))
    return memo[n]



print(fib(100))