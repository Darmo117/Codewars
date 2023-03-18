def to_utf8_binary(string: str) -> str:
    return ''.join(format(b, '08b') for b in string.encode('utf-8'))


def from_utf8_binary(bitstring: str) -> str:
    return bytes(int(bitstring[i:i + 8], 2) for i in range(0, len(bitstring), 8)).decode('utf-8')
