import datetime as dt


def unlucky_days(year):
    date = dt.date(year, 1, 1)
    nb = 0
    while date < dt.date(year + 1, 1, 1):
        if date.weekday() == 4 and date.day == 13:
            nb += 1
        date += dt.timedelta(days=1)
    return nb
