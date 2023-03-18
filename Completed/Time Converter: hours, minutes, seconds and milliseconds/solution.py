import datetime as dt


def convert(time: dt.datetime):
    return time.strftime(f'%H:%M:%S,{time.microsecond // 1000:03}')
