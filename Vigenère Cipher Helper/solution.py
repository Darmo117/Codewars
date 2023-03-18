import io


class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str):
        self._key = key
        self._alphabet = alphabet

    def encode(self, text: str) -> str:
        return self._shift(text, 1)

    def decode(self, text: str) -> str:
        return self._shift(text, -1)

    def _shift(self, text: str, direction: int):
        i = 0
        res = io.StringIO()
        alpha = self._alphabet
        for c in text:
            if c in alpha:
                new_i = (alpha.index(c) + alpha.index(self._key[i]) * direction) % len(alpha)
                res.write(alpha[new_i])
            else:
                res.write(c)
            i = (i + 1) % len(self._key)
        return res.getvalue()
