def interpreter(tape: str) -> str:
    data = [0] * 1000
    dp = 0
    output = ''
    for c in tape:
        match c:
            case '>':
                dp += 1
            case '<':
                dp -= 1
            case '+':
                data[dp] = (data[dp] + 1) % 256
            case '*':
                output += chr(data[dp])
    return output
