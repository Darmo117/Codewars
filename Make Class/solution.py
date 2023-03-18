def make_class(*args: str):
    class _DynamicClass:
        def __init__(self, *values):
            for i, n in enumerate(args):
                setattr(self, n, values[i])

    return _DynamicClass
