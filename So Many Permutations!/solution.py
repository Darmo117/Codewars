import itertools as it


def permutations(s):
    return [''.join(p) for p in set(it.permutations(s))]
