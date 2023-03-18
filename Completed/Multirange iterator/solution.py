import functools
import operator


def multiiter(*params: int):
    values = [0] * len(params)
    for i in range(functools.reduce(operator.mul, params, 1)):
        yield tuple(values)
        carry = False
        for j, (v, m) in enumerate(zip(reversed(values), reversed(params))):
            if j == 0 or carry:
                carry = v == m - 1
                values[-j - 1] = (values[-j - 1] + 1) % m
