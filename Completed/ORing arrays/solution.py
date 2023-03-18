def or_arrays(arr1: list[int], arr2: list[int], default: int = 0) -> list[int]:
    diff = len(arr1) - len(arr2)
    if diff < 0:
        arr1 += [default] * -diff
    elif diff > 0:
        arr2 += [default] * diff
    return [a | b for a, b in zip(arr1, arr2)]
