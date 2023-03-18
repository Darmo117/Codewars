class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert_nth(head: Node | None, index: int, data) -> Node:
    node = head
    prev = None
    i = 0
    while i < index and node:
        i += 1
        prev = node
        node = node.next
    if i < index:
        raise ValueError()
    n = Node(data, node)
    if prev:
        prev.next = n
        return head
    return n
