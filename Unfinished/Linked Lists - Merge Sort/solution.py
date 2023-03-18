class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data} -> {self.next}'


def merge_sort(list_: Node) -> Node:
    pass
