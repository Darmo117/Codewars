import datetime as dt


def age_in_days(year: int, month: int, day: int):
    diff = dt.datetime.now().date() - dt.date(year, month, day)
    return f'You are {diff.days} days old'
