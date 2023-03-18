def bits_battle(numbers: list[int]) -> str:
    odd_sum = 0
    even_sum = 0
    for n in numbers:
        if n == 0:
            continue
        if n % 2 == 0:
            even_sum += n.bit_length() - n.bit_count()
        else:
            odd_sum += n.bit_count()
    if odd_sum > even_sum:
        return 'odds win'
    if even_sum > odd_sum:
        return 'evens win'
    return 'tie'
