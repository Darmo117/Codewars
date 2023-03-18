def deep_count(a: list) -> int:
    nb = 0
    for e in a:
        if isinstance(e, list):
            nb += deep_count(e)
        nb += 1
    return nb
