import math


def bits_war(numbers: list[int]) -> str:
    odd_sum = 0
    even_sum = 0
    for n in numbers:
        strength = n.bit_count() * math.copysign(1, n)
        if n % 2 == 0:
            even_sum += strength
        else:
            odd_sum += strength
    if odd_sum > even_sum:
        return 'odds win'
    if even_sum > odd_sum:
        return 'evens win'
    return 'tie'
