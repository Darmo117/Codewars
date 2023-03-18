def decode_pass(pass_list: list[str], bits: str) -> str | bool:
    text = ''.join(chr(int(b, 2)) for b in bits.split())
    return text if text in pass_list else False
