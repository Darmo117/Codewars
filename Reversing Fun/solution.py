def reverse_fun(s: str) -> str:
    for i in range(len(s)):
        s = s[:i] + s[i:][::-1]
    return s
