def filter_homogenous(arrays: list) -> list:
    out = []
    for array in arrays:
        if len(set(map(type, array))) == 1:
            out.append(array)
    return out
