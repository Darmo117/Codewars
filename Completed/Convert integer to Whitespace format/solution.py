def whitespace_number(n: int) -> str:
    if n == 0:
        return ' \n'
    return (' ' if n > 0 else '\t') + format(abs(n), 'b').replace('0', ' ').replace('1', '\t') + '\n'
