def what_century(year: str) -> str:
    century = (int(year) - 1) // 100 + 1
    d = century % 10
    e = century // 10 % 10
    if d == 1 and e > 1:
        ending = 'st'
    elif d == 2 and e > 1:
        ending = 'nd'
    elif d == 3 and e > 1:
        ending = 'rd'
    else:
        ending = 'th'
    return str(century) + ending
