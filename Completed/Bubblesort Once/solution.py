def bubblesort_once(list_: list) -> list:
    list__ = list(list_)
    for i in range(len(list__) - 1):
        if list__[i] > list__[i + 1]:
            list__[i + 1], list__[i] = list__[i], list__[i + 1]
    return list__
