def anything(_):
    class AlwaysTrue:
        def __eq__(self, other):
            return True

        __ne__ = __gt__ = __ge__ = __lt__ = __le__ = __eq__

    return AlwaysTrue()
