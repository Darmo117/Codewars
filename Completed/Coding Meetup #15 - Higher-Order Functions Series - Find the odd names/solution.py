def find_odd_names(lst):
    return [user for user in lst if sum(ord(c) for c in user['firstName']) % 2 == 1]
