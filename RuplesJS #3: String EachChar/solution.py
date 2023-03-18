def each_char(string: str, arg) -> str:
    if isinstance(arg, str):
        f = lambda c: c + arg
    else:
        f = arg
    return ''.join(map(f, string))
