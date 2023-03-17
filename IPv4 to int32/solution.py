def ip_to_int32(ip: str) -> int:
    return int(''.join(f'{int(b):08b}' for b in ip.split('.')), 2)
