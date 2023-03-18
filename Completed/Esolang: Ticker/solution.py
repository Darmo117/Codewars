def interpreter(tape: str) -> str:
    data = [0]
    dp = 0
    output = ''

    def get_v():
        return data[dp] if 0 <= dp < len(data) else 0

    def set_v(n: int):
        if 0 <= dp < len(data):
            data[dp] = n

    for c in tape:
        match c:
            case '>':
                dp += 1
            case '<':
                dp -= 1
            case '+':
                set_v((get_v() + 1) % 256)
            case '-':
                set_v((get_v() - 1) % 256)
            case '/':
                set_v(0)
            case '!':
                data.append(0)
            case '*':
                output += chr(get_v())
    return output
