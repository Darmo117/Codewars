def limiter(limit: int, unique: str, lookup: str):
    def aux(cls):
        cls._instances = {}
        cls._last_returned = None

        # noinspection PyProtectedMember
        def new(true_cls, *args, **kwargs):
            print(args)
            o = super(cls, true_cls).__new__(cls)
            # noinspection PyArgumentList
            o.__init__(*args, **kwargs)
            attr_value = getattr(o, unique)
            print(attr_value)
            if attr_value in true_cls._instances:
                cls._last_returned = true_cls._instances[attr_value]
                return cls._last_returned
            if len(true_cls._instances) == limit:
                instances = list(true_cls._instances.values())
                if lookup == 'FIRST':
                    return instances[0]
                if lookup == 'LAST':
                    return instances[-1]
                if lookup == 'RECENT':
                    return true_cls._last_returned
                raise ValueError(f'invalid lookup value {lookup!r}')
            cls._last_returned = o
            true_cls._instances[attr_value] = o
            return o

        cls.__new__ = new

        return cls

    return aux
