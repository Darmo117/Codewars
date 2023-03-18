class Event:
    def __init__(self):
        self._callbacks = []

    def subscribe(self, f):
        self._callbacks.append(f)

    def unsubscribe(self, f):
        self._callbacks.remove(f)

    def emit(self, *args):
        for c in self._callbacks:
            c(*args)
