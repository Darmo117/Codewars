def sale_hotdogs(n: int) -> int:
    if n < 5:
        price = 100
    elif 5 <= n < 10:
        price = 95
    else:
        price = 90
    return price * n
