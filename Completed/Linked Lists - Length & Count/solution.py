class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node: Node | None) -> int:
    size = 0
    while node:
        size += 1
        node = node.next
    return size


def count(node: Node | None, data) -> int:
    nb = 0
    while node:
        if node.data == data:
            nb += 1
        node = node.next
    return nb
