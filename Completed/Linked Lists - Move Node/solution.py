class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Context:
    def __init__(self, source: Node, dest: Node | None):
        self.source = source
        self.dest = dest


def move_node(source: Node, dest: Node | None) -> Context:
    if not source:
        raise ValueError()
    new_source = source.next
    source.next = dest
    return Context(new_source, source)
