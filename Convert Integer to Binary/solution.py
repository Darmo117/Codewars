def to_binary(n: int) -> str:
    if n < 0:
        n = 2 ** 32 + n
    return f'{n:b}'
