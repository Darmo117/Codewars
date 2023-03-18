def rule30(values: list[int], n: int) -> list[int]:
    values.insert(0, 0)
    values.append(0)
    for _ in range(n):
        values.insert(0, 0)
        values.append(0)
        new = [0] * len(values)
        for i, v in enumerate(values[1:-1]):
            new[i + 1] = int(values[i:i + 3] in ([0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0]))
        values = new
    return values[1:-1]
