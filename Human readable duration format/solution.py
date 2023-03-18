def format_duration(seconds: int) -> str:
    if seconds == 0:
        return 'now'

    def f(d: int, s: str):
        if d:
            out.append(f'{d} {s}{"s" if d > 1 else ""}')

    out = []
    f(seconds // 31_536_000, 'year')
    f(seconds // 86400 % 365, 'day')
    f(seconds // 3600 % 24, 'hour')
    f(seconds // 60 % 60, 'minute')
    f(seconds % 60, 'second')
    if len(out) == 1:
        return out[0]
    return ', '.join(out[:-1]) + ' and ' + out[-1]
