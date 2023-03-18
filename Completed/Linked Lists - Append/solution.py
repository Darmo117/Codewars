class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def append(list_a: Node, list_b: Node) -> Node:
    if not list_a:
        return list_b
    elif not list_b:
        return list_a
    node = list_a
    while node.next:
        node = node.next
    node.next = list_b
    return list_a
