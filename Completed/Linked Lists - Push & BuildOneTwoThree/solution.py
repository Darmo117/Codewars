class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head: Node | None, data) -> Node:
    n = Node(data)
    n.next = head
    return n


def build_one_two_three() -> Node:
    return push(push(push(None, 3), 2), 1)
