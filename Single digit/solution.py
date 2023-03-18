def single_digit(n: int) -> int:
    while n > 9:
        n = n.bit_count()
    return n
