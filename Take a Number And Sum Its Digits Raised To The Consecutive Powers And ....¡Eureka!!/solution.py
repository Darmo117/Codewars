def is_eureka(n):
    return sum(int(d) ** i for i, d in enumerate(str(n), start=1)) == n


def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    return [n for n in range(a, b + 1) if is_eureka(n)]
