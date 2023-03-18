def reverse(lst):
    empty_list = list()
    for _ in range(len(lst)):
        empty_list.append(lst.pop())
    return empty_list
