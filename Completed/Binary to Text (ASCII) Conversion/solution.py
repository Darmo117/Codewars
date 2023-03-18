def binary_to_string(binary: str) -> str:
    text = ''
    for i in range(0, len(binary), 8):
        text += chr(int(binary[i:i + 8], 2))
    return text
