def is_same_language(lst):
    return len(set(user['language'] for user in lst)) == 1
