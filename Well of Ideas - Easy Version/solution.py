def well(x: list[str]):
    c = x.count('good')
    if c == 0:
        return 'Fail!'
    if c <= 2:
        return 'Publish!'
    return 'I smell a series!'
