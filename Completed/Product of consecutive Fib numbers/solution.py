# noinspection PyPep8Naming
def productFib(prod):
    a, b = 0, 1
    while True:
        if a * b == prod:
            return [a, b, True]
        if a * b > prod:
            return [a, b, False]
        a, b = b, a + b
