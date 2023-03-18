from __future__ import annotations


class Quark(object):
    baryon_number = 1 / 3

    def __init__(self, color: str, flavor: str):
        self._color = color
        self._flavor = flavor

    @property
    def color(self) -> str:
        return self._color

    @property
    def flavor(self) -> str:
        return self._flavor

    def interact(self, other: Quark):
        self._color, other._color = other.color, self.color
