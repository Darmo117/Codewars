import datetime as dt


def day_of_week(date: str) -> str:
    return dt.datetime.strptime(date, '%d/%m/%Y').strftime('%A')
