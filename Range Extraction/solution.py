def solution(values):
    res = []

    buffer = []
    # Add dummy non-integer value to avoid re-writing buffer-emptying statements after the loop
    for v in values + [0.1]:
        if not buffer:
            buffer.append(v)
        else:
            if v == buffer[-1] + 1:
                buffer.append(v)
            else:
                if len(buffer) == 1:
                    res.append(str(buffer[0]))
                elif len(buffer) == 2:
                    res.append(str(buffer[0]))
                    res.append(str(buffer[1]))
                else:
                    res.append(f'{buffer[0]}-{buffer[-1]}')
                buffer.clear()
                buffer.append(v)

    return ','.join(res)
