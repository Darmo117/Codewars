def remember(class_):
    class Meta(type):
        def __iter__(self):
            # noinspection PyUnresolvedReferences
            return iter(self._instances.keys())

        def __getitem__(self, item):
            # noinspection PyUnresolvedReferences
            return self._instances[item]

    class Wrapper(class_, metaclass=Meta):
        def __new__(cls, *args):
            if not hasattr(cls, '_instances'):
                cls._instances = {}
            if len(args) == 1:
                args = args[0]
            if args in cls._instances:
                return cls._instances[args]
            o = super().__new__(cls)
            cls._instances[args] = o
            return o

    return Wrapper
