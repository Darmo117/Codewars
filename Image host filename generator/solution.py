import random

_cache = []
_chars = ''.join(chr(i) for i in range(33, 127))


# noinspection PyPep8Naming
def generateName() -> str:
    stop = False
    name = ''
    while not stop:
        name = ''.join(random.choices(_chars, k=6))
        stop = name not in _cache
    return name
