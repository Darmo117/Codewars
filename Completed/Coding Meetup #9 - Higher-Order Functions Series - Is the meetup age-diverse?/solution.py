def is_age_diverse(lst):
    ages = set()
    for user in lst:
        a = user['age'] // 10
        if 1 <= a <= 9:
            ages.add(a)
        elif a >= 10:
            ages.add(10)
    return len(ages) == 10
