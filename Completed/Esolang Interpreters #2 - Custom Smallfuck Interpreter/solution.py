def interpreter(code: str, tape: str):
    tape_: list[int] = [int(c) for c in tape]
    tp = 0
    ip = 0
    while ip < len(code) and 0 <= tp < len(tape_):
        match code[ip]:
            case '<':
                tp -= 1
                ip += 1
            case '>':
                tp += 1
                ip += 1
            case '*':
                # Flip current bit
                tape_[tp] = 1 - tape_[tp]
                ip += 1
            case '[':
                if not tape_[tp]:
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
                if tape_[tp]:
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

    return ''.join(map(str, tape_))
