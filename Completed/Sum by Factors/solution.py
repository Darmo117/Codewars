def prime_factors(n: int) -> list[int]:
    factors = set()

    i = 2
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)

    return sorted(factors)


def sum_for_list(values: list[int]):
    factors = {v for n in values for v in prime_factors(abs(n))}
    res = []
    for p in sorted(factors):
        res.append([p, sum(n for n in values if n % p == 0)])
    return res
