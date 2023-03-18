def complete_binary_tree(array: list) -> list:
    array = array.copy()
    levels_nb = len(array).bit_length()
    # Remove bottom level’s items from array
    last_row_nb = 2 ** (levels_nb - 1) - (2 ** levels_nb - 1 - len(array))
    last_row = []
    for i in range(last_row_nb):
        last_row.append(array[i])
        del array[i]
    # Build a perfect tree from remaining items
    tree = []
    for i in range(1, levels_nb):
        start = len(array) // 2 ** i
        for j in range(start, len(array), 2 ** (levels_nb - i)):
            tree.append(array[j])
    # Add bottom row to the tree
    return tree + last_row
