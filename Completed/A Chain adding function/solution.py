# noinspection PyPep8Naming
class add(int):
    def __call__(self, n: int):
        return add(self + n)
