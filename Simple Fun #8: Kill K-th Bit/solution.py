def kill_kth_bit(n: int, k: int) -> int:
    return n & (2 ** 31 - 1 - 2 ** (k - 1))
