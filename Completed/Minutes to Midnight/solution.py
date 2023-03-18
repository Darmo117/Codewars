import datetime as dt


def minutes_to_midnight(d: dt.datetime):
    t = (d + dt.timedelta(days=1)).replace(hour=0, minute=0, second=0) - d
    return f'{round(t.seconds / 60)} minutes'
