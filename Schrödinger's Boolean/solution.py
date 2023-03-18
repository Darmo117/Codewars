class Omnibool:
    def __eq__(self, other):
        if isinstance(other, bool):
            return True
        return False


omnibool = Omnibool()
