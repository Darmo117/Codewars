import math


def score(n):
    return n | (2 ** math.floor(math.log2(n)) - 1) if n != 0 else 0
