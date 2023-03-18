def cute_pattern(tiles: str):
    if 'BB' in tiles:
        return False
    return not any(tiles[i] == tiles[i + 4] == 'B' or tiles[i + 8] == tiles[i + 12] == 'B' for i in range(4))
