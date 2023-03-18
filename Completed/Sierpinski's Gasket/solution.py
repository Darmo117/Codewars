def sierpinski(n):
    row = [1]
    res = ''
    for _ in range(2 ** n):
        res += ' '.join(' L'[cell % 2] for cell in row) + '\n'
        next_row = [1] * (len(row) + 1)
        for i in range(1, len(next_row) - 1):
            next_row[i] = row[i - 1] + row[i]
        row = next_row
    return res[:-1]  # Remove trailing \n
