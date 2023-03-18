import datetime as dt


def timer(limit: int):
    def wrapper(f):
        def surrogate(*args, **kwargs):
            start = dt.datetime.now().timestamp()
            f(*args, **kwargs)
            return dt.datetime.now().timestamp() - start <= limit

        return surrogate

    return wrapper
