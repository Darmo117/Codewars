def zero(f=None):
    return f(zero()) if f else 0


def one(f=None):
    return f(one()) if f else 1


def two(f=None):
    return f(two()) if f else 2


def three(f=None):
    return f(three()) if f else 3


def four(f=None):
    return f(four()) if f else 4


def five(f=None):
    return f(five()) if f else 5


def six(f=None):
    return f(six()) if f else 6


def seven(f=None):
    return f(seven()) if f else 7


def eight(f=None):
    return f(eight()) if f else 8


def nine(f=None):
    return f(nine()) if f else 9


def plus(v: int):
    return lambda x: x + v


def minus(v: int):
    return lambda x: x - v


def times(v: int):
    return lambda x: x * v


def divided_by(v: int):
    return lambda x: x // v
