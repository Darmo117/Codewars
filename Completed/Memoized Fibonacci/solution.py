cache = [0, 1]


def fibonacci(n):
    if n < len(cache):
        return cache[n]
    a, b = cache[-2:]
    for _ in range(len(cache) - 1, n + 1):
        a, b = b, a + b
        cache.append(b)
    return a
