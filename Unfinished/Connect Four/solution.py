def who_is_winner(actions):
    grid = [['-'] * 7 for _ in range(6)]
    for action in actions:
        column = ord(action[0]) - ord('A')
        color = action[2]
        i = len(grid) - 1
        while grid[i][column] != '-':  # Seek empty line index for column
            i -= 1
        grid[i][column] = color
        print(i, column)
        print('\n'.join(''.join(line) for line in grid))
        if i <= 2:
            if all(grid[i + j][column] == color for j in range(4)):  # Check column
                return color
            if column >= 3 and all(grid[i + j][column - j] == color for j in range(4)):  # Check lower-left diagonal
                return color
            if column <= 3 and all(grid[i + j][column + j] == color for j in range(4)):  # Check lower-right diagonal
                return color
        if i >= 3:
            if column >= 3 and all(grid[i - j][column - j] == color for j in range(4)):  # Check upper-left diagonal
                return color
            if column <= 3 and all(grid[i - j][column + j] == color for j in range(4)):  # Check upper-right diagonal
                return color
        if column >= 3 and all(grid[i][column - j] == color for j in range(4)):  # Check left-side of line
            return color
        if column <= 3 and all(grid[i][column + j] == color for j in range(4)):  # Check right-side of line
            return color
    return 'Draw'


if __name__ == '__main__':
    print(who_is_winner([
        "F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red",
        "B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red",
        "F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red",
        "A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red",
        "B_Yellow", "B_Red"
    ]))
