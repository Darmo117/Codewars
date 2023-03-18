def draw(n):
    rows = [' _' * n + ' ']
    for i in range(1, 2 ** (n - 1) + 1):
        row = '|'
        for j in range(n - 1, -1, -1):
            m = i % (2 ** j)
            if m == 0:
                row += '_|'
            elif m > 2 ** (j - 1):
                row += ' |'
            else:
                row += '  '
        rows.append(row)
    return '\n'.join(rows)
