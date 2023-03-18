import struct


# noinspection PyPep8Naming
def float_to_IEEE_754(f: float) -> str:
    b, = struct.unpack('!Q', struct.pack('!d', f))
    print(b, f'{b:064b}')
    return f'{b >> 63} {(b >> 52) & 0x7ff:011b} {b & 0xfffffffffffff:052b}'
