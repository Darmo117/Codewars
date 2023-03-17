import math


def poohbear(code: str) -> str:
    tape: list[int] = [0] * 30000
    dp = len(tape) // 2
    ip = 0
    res = ''
    copy_cache = 0
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
            case 'c':
                copy_cache = tape[dp]
                ip += 1
            case 'p':
                tape[dp] = copy_cache
                ip += 1
            case 'P':
                res += chr(tape[dp])
                ip += 1
            case 'N':
                res += str(tape[dp])
                ip += 1
            case 'T':
                tape[dp] = (tape[dp] * 2) % 256
                ip += 1
            case 'Q':
                tape[dp] = (tape[dp] ** 2) % 256
                ip += 1
            case 'U':
                tape[dp] = math.floor(math.sqrt(tape[dp]))
                ip += 1
            case 'L':
                tape[dp] = (tape[dp] + 2) % 256
                ip += 1
            case 'I':
                tape[dp] = (tape[dp] - 2) % 256
                ip += 1
            case 'V':
                tape[dp] //= 2
                ip += 1
            case 'A':
                tape[dp] = (tape[dp] + copy_cache) % 256
                ip += 1
            case 'B':
                tape[dp] = (tape[dp] - copy_cache) % 256
                ip += 1
            case 'Y':
                tape[dp] = (tape[dp] * copy_cache) % 256
                ip += 1
            case 'D':
                tape[dp] //= copy_cache
                ip += 1
            case 'W':
                if not tape[dp]:
                    n = 1
                    while n:  # Jump past matching ']'
                        ip += 1
                        match code[ip]:
                            case 'W':
                                n += 1
                            case 'E':
                                n -= 1
                ip += 1
            case 'E':
                if tape[dp]:
                    n = 1
                    while n:  # Jump back to matching '['
                        ip -= 1
                        match code[ip]:
                            case 'W':
                                n -= 1
                            case 'E':
                                n += 1
                else:
                    ip += 1
            case _:
                ip += 1

    return res
