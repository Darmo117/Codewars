def fractran(code: str, n: int) -> int:
    fracs = [tuple(map(int, f.split('/'))) for f in code.split()]
    stop = False
    i = 0
    while not stop and i < 1000:
        for f in fracs:
            if (n * f[0]) % f[1] == 0:
                n = (n * f[0]) // f[1]
                break
        else:
            stop = True
        i += 1
    return n
