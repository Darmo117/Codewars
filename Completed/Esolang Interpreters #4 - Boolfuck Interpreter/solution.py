def boolfuck(code: str, input: str = '') -> str:
    input_: list[int] = [int(b) for c in reversed(input) for b in format(ord(c), '08b')]
    tape: list[int] = [0] * 30000
    ip = 0
    dp = len(tape) // 2
    output: list[int] = []
    while ip < len(code):
        match code[ip]:
            case '<':
                dp -= 1
                ip += 1
            case '>':
                dp += 1
                ip += 1
            case '+':
                # Flip current bit
                tape[dp] = 1 - tape[dp]
                ip += 1
            case ';':
                output.insert(0, tape[dp])
                ip += 1
            case ',':
                tape[dp] = input_.pop() if input_ else 0
                ip += 1
            case '[':
                if not tape[dp]:
                    n = 1
                    while n:  # Jump past matching ']'
                        ip += 1
                        match code[ip]:
                            case '[':
                                n += 1
                            case ']':
                                n -= 1
                ip += 1
            case ']':
                if tape[dp]:
                    n = 1
                    while n:  # Jump back to matching '['
                        ip -= 1
                        match code[ip]:
                            case '[':
                                n -= 1
                            case ']':
                                n += 1
                else:
                    ip += 1
            case _:
                ip += 1

    if (r := len(output) % 8) != 0:
        output = [0] * (8 - r) + output
    res = ''
    for i in range(0, len(output), 8):
        res = chr(int(''.join(map(str, output[i:i + 8])), 2)) + res
    return res
