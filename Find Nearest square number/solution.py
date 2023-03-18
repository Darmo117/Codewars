import math


def nearest_sq(n):
    root = math.sqrt(n)
    before = math.floor(root) ** 2
    after = math.ceil(root) ** 2
    if n - before <= after - n:
        return before
    return after
