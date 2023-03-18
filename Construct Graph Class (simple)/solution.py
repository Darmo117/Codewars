class IllegalArgumentError(ValueError):
    pass


class Graph:
    def __init__(self, v: int):
        if v < 0:
            raise IllegalArgumentError()
        self.V = v
        self.E = 0
        self.adj = [[] for _ in range(v)]

    def add_edge(self, v: int, w: int):
        if not (0 <= v <= self.V) or not (0 <= w <= self.V):
            raise IllegalArgumentError()
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1
