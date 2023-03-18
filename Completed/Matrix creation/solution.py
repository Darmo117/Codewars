def get_matrix(n: int) -> list[list[int]]:
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
        matrix[-1][i] = 1
    return matrix
