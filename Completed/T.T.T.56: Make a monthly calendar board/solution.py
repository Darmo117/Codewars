import calendar as cal
import datetime as dt


def calendar(year: int, month: int) -> str:
    days_row = 'SUN MON TUE WED THU FRI SAT'
    res = f'{year} {cal.month_name[month]}'
    res = ' ' * ((len(days_row) - len(res)) // 2) + res
    res += '\n' + days_row + '\n'
    date = dt.date(year, month, 1)
    last_day = cal.monthrange(year, month)[1]
    for day in range(1, last_day + 1):
        date = date.replace(day=day)
        weekday = (date.weekday() + 1) % 7  # Make week start on sunday instead of monday
        if day == 1:  # Offset before first day
            res += ' ' * (weekday * 4)
        if day < 10:
            res += f' {day}'
            if weekday < 6:  # Do not add trailing space if last in row
                res += ' '
        else:
            res += f' {day}'
        if day < last_day:  # Do not add separator after last day
            if weekday == 6:
                res += '\n'
            else:
                res += ' '
    return res
