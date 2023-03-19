def cube_odd(arr: list) -> int | None:
    print(arr)
    s = 0
    for v in arr:
        if type(v) is not int:
            return None
        if v % 2 == 1:
            s += v ** 3
    return s
