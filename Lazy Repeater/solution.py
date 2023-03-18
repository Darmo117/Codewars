def make_looper(string: str):
    class Generator:
        def __init__(self, s: str):
            self._s = s
            self._i = 0

        def __call__(self):
            v = self._s[self._i]
            self._i = (self._i + 1) % len(self._s)
            return v

    return Generator(string)
