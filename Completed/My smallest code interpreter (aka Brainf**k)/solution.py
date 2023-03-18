def brain_luck(code: str, program_input: str) -> str:
    input_: list[str] = list(program_input[::-1])
    tape: list[int] = [0] * 30000
    dp = 0
    ip = 0
    res = ''
    while ip < len(code):
        match code[ip]:
            case '<':
                dp -= 1
                ip += 1
            case '>':
                dp += 1
                ip += 1
            case '+':
                tape[dp] = (tape[dp] + 1) % 256
                ip += 1
            case '-':
                tape[dp] = (tape[dp] - 1) % 256
                ip += 1
            case '.':
                res += chr(tape[dp])
                ip += 1
            case ',':
                tape[dp] = ord(input_.pop())
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

    return res
