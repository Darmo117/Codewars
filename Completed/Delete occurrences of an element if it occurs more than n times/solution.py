def delete_nth(values, max_occ):
    occs = {}
    vs = []
    for v in values:
        if (absent := v not in occs) or occs[v] < max_occ:
            vs.append(v)
            if absent:
                occs[v] = 0
            occs[v] += 1
    return vs
