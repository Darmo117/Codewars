import random


def throw_rigged() -> int:
    v = random.random()
    if 0 <= v <= 0.22:
        return 6
    return 1
