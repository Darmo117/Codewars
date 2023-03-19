def chained(functions):
    def func(arg):
        res = arg
        for f in functions:
            res = f(res)
        return res

    return func
