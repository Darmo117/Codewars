def func(n: int) -> bool:
    return n % 2 == 0


# noinspection PyShadowingBuiltins
def map(arr: list[int], somefunction) -> list | str:
    if not callable(somefunction):
        return 'given argument is not a function'
    res = []
    for v in arr:
        try:
            v = int(v)
        except ValueError:
            return 'array should contain only numbers'
        res.append(somefunction(v))
    return res
