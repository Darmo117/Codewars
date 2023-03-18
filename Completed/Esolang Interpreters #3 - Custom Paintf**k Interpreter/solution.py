def interpreter(code, iterations, width, height):
    grid = [[0] * width for _ in range(height)]
    gp = [0, 0]
    ip = 0
    i = 0
    while i < iterations and ip < len(code):
        skipped = False
        c = code[ip]
        match c:
            case 'n':
                gp[0] = (gp[0] - 1) % height
                ip += 1
            case 's':
                gp[0] = (gp[0] + 1) % height
                ip += 1
            case 'w':
                gp[1] = (gp[1] - 1) % width
                ip += 1
            case 'e':
                gp[1] = (gp[1] + 1) % width
                ip += 1
            case '*':
                # Swap current bit
                grid[gp[0]][gp[1]] = 1 - grid[gp[0]][gp[1]]
                ip += 1
            case '[':
                if not grid[gp[0]][gp[1]]:
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
                if grid[gp[0]][gp[1]]:
                    n = 1
                    while n:  # Jump back to matching '['
                        ip -= 1
                        match code[ip]:
                            case '[':
                                n -= 1
                            case ']':
                                n += 1
                    i -= 1  # Don’t count this iteration as the next one start after the '['
                else:
                    ip += 1
            case _:
                skipped = True
                ip += 1
        if not skipped:
            i += 1

    return '\r\n'.join(''.join(str(b) for b in row) for row in grid)
