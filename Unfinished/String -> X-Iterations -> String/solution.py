def reverse_fun(s: str) -> str:
    for i in range(len(s)):
        s = s[:i] + s[i:][::-1]
    return s


def string_func(s: str, x: int) -> str:
    for _ in range(x):
        s = reverse_fun(s)
    return s
