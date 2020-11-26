import timeit


def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def fib_memo(n, cache=None):
    if n == 0:
        return 1
    if n == 1:
        return 1

    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]

    result = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    cache[n] = result
    return result


def fib_bottom_up(n):
    a = 1
    b = 1
    for i in range(2, n+1):
        a, b = b, a + b

    return b


print(timeit.timeit('fib_bottom_up(10)', number=100, globals=globals()))
print(timeit.timeit('fib_bottom_up(20)', number=100, globals=globals()))
print(timeit.timeit('fib_bottom_up(30)', number=100, globals=globals()))
