import collections


def count_languages(lst):
    return collections.Counter(user['language'] for user in lst)
