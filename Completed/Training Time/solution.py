def shuffle_it(values: list, *swaps: list):
    values = list(values)
    for i1, i2 in swaps:
        values[i1], values[i2] = values[i2], values[i1]
    return values
