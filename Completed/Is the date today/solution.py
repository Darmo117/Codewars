import datetime as dt


def is_today(date):
    return date.date() == dt.datetime.now().date()
