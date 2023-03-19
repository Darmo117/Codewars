import collections


def is_language_diverse(lst):
    counts = collections.Counter(user['language'] for user in lst)
    maxi = max(counts.values())
    return all(maxi <= 2 * c for c in counts.values())
