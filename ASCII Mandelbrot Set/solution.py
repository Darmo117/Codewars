def iterate(c: complex, max_iter: int) -> int:
    z = 0
    for i in range(max_iter):
        z = z ** 2 + c
        if abs(z) >= 2:
            return i
    return max_iter


def mandelbrot_string(xc: float, yc: float, width: int, height: int, step_size: float, max_iter: int) -> str:
    chars = ' ░▒▓█'
    rows = []

    for i in range(-height, height + 1):
        y = yc + -i * step_size * 2
        row = ''
        for j in range(-width, width + 1):
            x = xc + j * step_size
            iterations = iterate(complex(x, y), max_iter)
            row += chars[4 * iterations // max_iter]
        rows.append(row)

    return '\n'.join(rows)
