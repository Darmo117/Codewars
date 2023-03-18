# noinspection PyPep8Naming
class Url_shortener:
    def __init__(self):
        self._mappings = {}
        self._reverse_mappings = {}
        self._code_seed = [0, -1, -1, -1]

    def shorten(self, long_url: str) -> str:
        short_code = self._reverse_mappings.get(long_url, None)
        if short_code is None:
            short_code = ''.join(chr(97 + int(i)) for i in self._code_seed if i != -1)
            carry = False
            for i in range(len(self._code_seed)):
                if i == 0 or carry:
                    carry = self._code_seed[i] == 25
                    self._code_seed[i] = (self._code_seed[i] + 1) % 26
            self._mappings[short_code] = long_url
            self._reverse_mappings[long_url] = short_code
        return f'short.ly/{short_code}'

    def redirect(self, short_url: str) -> str:
        short_code = short_url.split('/', maxsplit=1)[1]
        return self._mappings[short_code]
