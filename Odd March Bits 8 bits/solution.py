def bit_march(n: int) -> list[list[int]]:
    steps = []
    for i in range(8 - n + 1):
        steps.append([0] * (8 - i - n) + [1] * n + [0] * i)
    return steps
