from __future__ import annotations

import math


class Vector:
    def __init__(self, values: list[int | float]):
        self._values = list(values)

    def add(self, other: Vector) -> Vector:
        return Vector([a + b for a, b in zip(self._values, other._values)])

    def subtract(self, other: Vector) -> Vector:
        return Vector([a - b for a, b in zip(self._values, other._values)])

    def dot(self, other: Vector) -> int | float:
        return sum(a * b for a, b in zip(self._values, other._values))

    def norm(self) -> float:
        return math.sqrt(sum(v ** 2 for v in self._values))

    def equals(self, other: Vector) -> bool:
        return self._values == other._values

    def __str__(self):
        return f'({",".join(map(str, self._values))})'
