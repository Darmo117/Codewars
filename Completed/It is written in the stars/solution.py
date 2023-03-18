import datetime as dt


def star_sign(date: dt.date) -> str:
    y = date.year
    if dt.date(y, 1, 21) <= date <= dt.date(y, 2, 19):
        return 'Aquarius'
    elif dt.date(y, 2, 20) <= date <= dt.date(y, 3, 20):
        return 'Pisces'
    elif dt.date(y, 3, 21) <= date <= dt.date(y, 4, 20):
        return 'Aries'
    elif dt.date(y, 4, 21) <= date <= dt.date(y, 5, 21):
        return 'Taurus'
    elif dt.date(y, 5, 22) <= date <= dt.date(y, 6, 21):
        return 'Gemini'
    elif dt.date(y, 6, 22) <= date <= dt.date(y, 7, 22):
        return 'Cancer'
    elif dt.date(y, 7, 23) <= date <= dt.date(y, 8, 23):
        return 'Leo'
    elif dt.date(y, 8, 24) <= date <= dt.date(y, 9, 23):
        return 'Virgo'
    elif dt.date(y, 9, 24) <= date <= dt.date(y, 10, 23):
        return 'Libra'
    elif dt.date(y, 10, 24) <= date <= dt.date(y, 11, 22):
        return 'Scorpio'
    elif dt.date(y, 11, 23) <= date <= dt.date(y, 12, 21):
        return 'Sagittarius'
    else:
        return 'Capricorn'
