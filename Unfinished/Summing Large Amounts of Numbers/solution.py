def sum_them(n):
    total = 0
    for x in range(2 ** n):
        total += (x ^ (x // 2))
    return total
