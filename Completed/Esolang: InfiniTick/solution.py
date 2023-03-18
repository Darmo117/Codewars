def interpreter(tape: str) -> str:
    data = [0] * 100000
    dp = len(data) // 2
    output = ''
    i = 0
    while True:
        match tape[i]:
            case '>':
                dp += 1
            case '<':
                dp -= 1
            case '+':
                data[dp] = (data[dp] + 1) % 256
            case '-':
                data[dp] = (data[dp] - 1) % 256
            case '*':
                output += chr(data[dp])
            case '&':
                break
            case '/':
                if not data[dp]:
                    i = (i + 1) % len(tape)
            case '\\':
                if data[dp]:
                    i = (i + 1) % len(tape)
        i = (i + 1) % len(tape)
    return output
