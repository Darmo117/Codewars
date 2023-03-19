to_celcius = {
    'C': lambda t: t,
    'F': lambda t: (t - 32) * 5 / 9,
    'K': lambda t: t - 273.15,
    'R': lambda t: (t - 491.67) * 5 / 9,
    'De': lambda t: 100 - t * 2 / 3,
    'N': lambda t: t * 100 / 33,
    'Re': lambda t: t * 5 / 4,
    'Ro': lambda t: (t - 7.5) * 40 / 21,
}
from_celcius = {
    'C': lambda t: t,
    'F': lambda t: t * 9 / 5 + 32,
    'K': lambda t: t + 273.15,
    'R': lambda t: (t + 273.15) * 9 / 5,
    'De': lambda t: (100 - t) * 2 / 3,
    'N': lambda t: t * 33 / 100,
    'Re': lambda t: t * 4 / 5,
    'Ro': lambda t: t * 27 / 40 + 7.5
}


def convert_temp(temp: float, from_scale: str, to_scale: str) -> float:
    return round(from_celcius[to_scale](to_celcius[from_scale](temp)))
