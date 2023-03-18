import math


def page_digits(pages: int) -> int:
    p = math.floor(math.log10(pages))
    tens = sum(9 * (i + 1) * 10 ** i for i in range(p))
    remainder = (p + 1) * (pages - 10 ** p) + p + 1
    return tens + remainder
