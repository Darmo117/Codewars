class Cipher(object):
    def __init__(self, map1, map2):
        self._map1 = map1
        self._map2 = map2

    def encode(self, s):
        return self._cypher(self._map2, self._map1, s)

    def decode(self, s):
        return self._cypher(self._map1, self._map2, s)

    @staticmethod
    def _cypher(m1, m2, s):
        return ''.join(m1[m2.index(c)] if c in m2 else c for c in s)
