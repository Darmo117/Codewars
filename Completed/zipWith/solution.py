def zip_with(fn, a1: list, a2: list) -> list:
    return [fn(a, b) for a, b in zip(a1, a2)]
