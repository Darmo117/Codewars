def positive_to_negative(binary: list[int]) -> list[int]:
    carry = 1
    res = [0] * len(binary)
    for i, b in enumerate(binary[::-1]):
        c = carry + 1 - b
        carry = c >> 1
        res[len(res) - i - 1] = c & 1
    return res
