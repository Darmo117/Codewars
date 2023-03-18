def range_bit_count(a: int, b: int) -> int:
    return sum(i.bit_count() for i in range(a, b + 1))
