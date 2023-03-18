class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head: Node | None) -> Node | None:
    values = set()
    node = head
    prev = None
    while node:
        if node.data in values:
            n = node.next
            if prev:
                prev.next = n
            node = n
        else:
            values.add(node.data)
            prev = node
            node = node.next
    return head
