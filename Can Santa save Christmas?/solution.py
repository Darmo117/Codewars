import datetime as dt


def determine_time(arr: list[str]) -> bool:
    total = dt.timedelta()
    for t in arr:
        h, m, s = map(int, t.split(':'))
        total += dt.timedelta(hours=h, minutes=m, seconds=s)
    return total.total_seconds() <= 86400
