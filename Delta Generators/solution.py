def delta(values, n: int):
    sentinel = object()
    iter_ = iter(values)
    diffs = [[] for _ in range(n + 1)]
    while (v := next(iter_, sentinel)) is not sentinel:
        diffs[0].append(v)
        for i in range(1, n + 1):
            if len(diffs[i - 1]) > 1:
                diffs[i].append(diffs[i - 1][-1] - diffs[i - 1][-2])
        if diffs[-1]:
            yield diffs[-1][-1]
