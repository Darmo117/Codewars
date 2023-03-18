def flatten(arr: list[list]) -> list:
    out = []
    for v in arr:
        if isinstance(v, list):
            out.extend(v)
        else:
            out.append(v)
    return out
