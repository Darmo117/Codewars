def fractalize(seed: list[str], size: int) -> list[str]:
    h = len(seed)
    w = len(seed[0])
    rows = []
    for r in range(h ** size):
        row = ''
        for c in range(w ** size):
            filled = True
            for i in range(size, 0, -1):
                if seed[r // (h ** (size - i)) % h][c // (w ** (size - i)) % w] == '.':
                    filled = False
                    break
            if filled:
                row += '*'
            else:
                row += '.'
        rows.append(row)
    return rows


if __name__ == '__main__':
    # print('\n'.join(fractalize(['**', '*.'], 8)))
    # print()
    print('\n'.join(fractalize(['*.*', '.*.', '*.*'], 6)))
    # print()
    # print('\n'.join(fractalize(['***', '*.*', '***'], 4)))
