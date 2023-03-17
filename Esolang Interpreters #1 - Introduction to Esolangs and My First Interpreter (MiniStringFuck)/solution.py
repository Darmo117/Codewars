def my_first_interpreter(code: str):
    cell = 0
    res = ''
    for c in code:
        match c:
            case '+':
                cell = (cell + 1) % 256
            case '.':
                res += chr(cell)
    return res
