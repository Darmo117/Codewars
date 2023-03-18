from __future__ import annotations


def create_number_class(digits: str) -> type:
    class _Number:
        _digits = digits
        _base = len(digits)

        def __init__(self, value: str):
            self._value = value
            self._int_value = self._to_int(value)

        @classmethod
        def _to_int(cls, s: str) -> int:
            i = 0
            for p, c in enumerate(s[::-1]):
                i += cls._digits.index(c) * cls._base ** p
            return i

        @classmethod
        def _from_int(cls, i: int) -> str:
            s = ''
            while i >= cls._base:
                i, r = divmod(i, cls._base)
                s = cls._digits[r] + s
            return cls._digits[i] + s

        def convert_to(self, cls: type[_Number]) -> _Number:
            return cls(cls._from_int(self._int_value))

        def __add__(self, other: _Number) -> _Number:
            return self._op(self._int_value + other._int_value)

        def __sub__(self, other: _Number) -> _Number:
            return self._op(self._int_value - other._int_value)

        def __mul__(self, other: _Number) -> _Number:
            return self._op(self._int_value * other._int_value)

        def __floordiv__(self, other: _Number) -> _Number:
            return self._op(self._int_value // other._int_value)

        @classmethod
        def _op(cls, i: int) -> _Number:
            return _Number(cls._from_int(i))

        def __str__(self):
            return self._value

    return _Number
