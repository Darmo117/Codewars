# noinspection PyUnresolvedReferences
from preloaded import TEXT2HEX

HEX2TEXT = {v: k for k, v in TEXT2HEX.items()}


class HexCipher:
    @classmethod
    def encode(cls, text: str, n: int) -> str:
        for _ in range(n):
            text = ''.join(TEXT2HEX[c] for c in text)
        return text

    @classmethod
    def decode(cls, text: str, n: int) -> str:
        for _ in range(n):
            text = ''.join(HEX2TEXT[text[i:i + 2]] for i in range(0, len(text), 2))
        return text
