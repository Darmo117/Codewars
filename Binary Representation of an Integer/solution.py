def show_bits(n: int) -> list[int]:
    if n < 0:
        n = 2 ** 32 + n
    return list(map(int, f'{n:032b}'))
