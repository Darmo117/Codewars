class HighScoreTable:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._scores = []

    @property
    def scores(self) -> list:
        return self._scores.copy()

    def update(self, score):
        for i in range(len(self._scores)):
            if score >= self._scores[i]:
                self._scores.insert(i, score)
                if len(self._scores) > self._capacity:
                    self._scores.pop()
                break
        else:
            if len(self._scores) < self._capacity:
                self._scores.append(score)

    def reset(self):
        self._scores.clear()
