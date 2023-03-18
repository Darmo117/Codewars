import itertools


def gen(n: int, iterable) -> tuple[int, ...]:
    iter_ = iter(itertools.cycle(iterable))
    cache = tuple(next(iter_) for _ in range(n))
    while True:
        yield cache
        cache = cache[1:] + (next(iter_),)
