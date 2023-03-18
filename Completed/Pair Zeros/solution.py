def pair_zeros(arr: list[int]) -> list[int]:
    out = []
    pairing = False
    for i in arr:
        if i == 0:
            if pairing:
                pairing = False
                continue
            pairing = True
        out.append(i)
    return out
