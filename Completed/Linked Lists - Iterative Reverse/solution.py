class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def reverse(head: Node):
    values = []
    node = head
    while node:
        values.append(node.data)
        node = node.next
    node = head
    i = len(values) - 1
    while node:
        node.data = values[i]
        i -= 1
        node = node.next
