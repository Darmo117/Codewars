def naughty_or_nice(data: dict[str, dict[str, str]]) -> str:
    naughties = 0
    nices = 0
    for days in data.values():
        for state in days.values():
            if state == 'Naughty':
                naughties += 1
            else:
                nices += 1
    if naughties > nices:
        return 'Naughty!'
    return 'Nice!'
