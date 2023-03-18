def multiply_all(arr: list[int]):
    def mul(n: int) -> list[int]:
        return [i * n for i in arr]

    return mul
