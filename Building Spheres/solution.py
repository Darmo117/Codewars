import math


class Sphere:
    def __init__(self, radius: int | float, mass: int | float):
        self._radius = radius
        self._mass = mass
        self._volume = 4 / 3 * math.pi * radius ** 3
        self._area = 4 * math.pi * self._radius ** 2
        self._density = mass / self._volume

    def get_radius(self) -> int | float:
        return self._radius

    def get_mass(self) -> int | float:
        return self._mass

    def get_volume(self) -> float:
        return round(self._volume, 5)

    def get_surface_area(self) -> float:
        return round(self._area, 5)

    def get_density(self) -> float:
        return round(self._density, 5)
