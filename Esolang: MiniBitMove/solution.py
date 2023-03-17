def interpreter(tape: str, array: str) -> str:
    data = list(map(int, array))
    dp = 0
    i = 0
    while dp < len(data):
        c = tape[i]
        if c == '1':
            data[dp] = 1 - data[dp]
        elif c == '0':
            dp += 1
        i = (i + 1) % len(tape)
    return ''.join(map(str, data))
