def byte_to_set(byte: int) -> set[int]:
    return {i for i in range(8) if f'{byte:08b}'[i] == '1'}
