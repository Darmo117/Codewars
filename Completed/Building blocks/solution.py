class Block:
    def __init__(self, dimensions: list[int]):
        self._w, self._l, self._h = dimensions

    def get_width(self) -> int:
        return self._w

    def get_length(self) -> int:
        return self._l

    def get_height(self) -> int:
        return self._h

    def get_volume(self) -> int:
        return self._w * self._l * self._h

    def get_surface_area(self) -> int:
        return 2 * (self._w * self._l + self._w * self._h + self._l * self._h)
