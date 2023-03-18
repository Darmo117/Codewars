DIRECTION_UP, DIRECTION_LEFT, DIRECTION_DOWN, DIRECTION_RIGHT = range(1, 5)


class Table:
    def __init__(self, data: list[list]):
        self.data = data
        self.ranges = {
            DIRECTION_DOWN: (len(data),),
            DIRECTION_UP: (len(data) - 1, -1, -1),
            DIRECTION_RIGHT: (len(data[0]),),
            DIRECTION_LEFT: (len(data[0]) - 1, -1, -1),
        }

    def walk(self, dir0: str, dir1: str):
        if dir0 in (DIRECTION_DOWN, DIRECTION_UP):
            yield from self._walk_rc(dir0, dir1)
        else:
            yield from self._walk_cr(dir0, dir1)

    def _walk_rc(self, dir0: str, dir1: str):
        for c in range(*self.ranges[dir1]):
            for r in range(*self.ranges[dir0]):
                yield self.data[r][c]

    def _walk_cr(self, dir0: str, dir1: str):
        for r in range(*self.ranges[dir1]):
            for c in range(*self.ranges[dir0]):
                yield self.data[r][c]
