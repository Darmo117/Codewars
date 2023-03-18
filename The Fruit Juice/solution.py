class Jar:
    def __init__(self):
        self._amounts = {}

    def add(self, amount: int | float, kind: str):
        if kind not in self._amounts:
            self._amounts[kind] = amount
        else:
            self._amounts[kind] += amount

    def pour_out(self, amount: int | float):
        # Cache concentrations as they would vary with each amount update in the following loop and mess everything up
        concentrations = {}
        for k, v in self._amounts.items():
            concentrations[k] = self.get_concentration(k)
        for k, v in self._amounts.items():
            if v != 0:
                self._amounts[k] -= amount * concentrations[k]

    def get_total_amount(self) -> float:
        return sum(self._amounts.values())

    def get_concentration(self, kind: str) -> float:
        total_amount = self.get_total_amount()
        if total_amount == 0:
            return 0
        return self._amounts.get(kind, 0) / total_amount
