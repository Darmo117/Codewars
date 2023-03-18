def shared_bits(a: int, b: int) -> bool:
    return (a & b).bit_count() >= 2
