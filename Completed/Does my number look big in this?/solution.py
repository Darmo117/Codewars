def narcissistic(n):
    digits = list(int(d) for d in str(n))
    p = len(digits)
    return sum(d ** p for d in digits) == n
