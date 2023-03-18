class Router:
    def __init__(self):
        self._binds = {}

    def bind(self, path: str, method: str, action):
        self._binds[path, method] = action

    # noinspection PyPep8Naming
    def runRequest(self, path: str, method: str):
        return self._binds.get((path, method), lambda: 'Error 404: Not Found')()
