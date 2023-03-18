import datetime as dt


def movie_times(open_t: int, close_t: int, length: int) -> list[tuple[int, int]]:
    t = dt.timedelta(minutes=length + 15)
    d = dt.datetime(2000, 1, 1, hour=open_t)
    res = []
    while d.hour < close_t:
        res.append((d.hour, d.minute))
        d += t
    return res
