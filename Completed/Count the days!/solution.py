import datetime as dt


def count_days(d: dt.datetime) -> str:
    t = d - dt.datetime.now()
    days = round(t.total_seconds() / 86400)
    if days < 0:
        return 'The day is in the past!'
    if days == 0:
        return 'Today is the day!'
    return f'{days} days'
