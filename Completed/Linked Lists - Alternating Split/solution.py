class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = next


class Context:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head: Node) -> Context:
    if not head or not head.next:
        raise ValueError()
    l1 = None
    l1head = None
    l2 = None
    l2head = None
    i = 0
    node = head
    while node:
        n = node.next
        if i % 2 == 0:
            if not l1:
                l1 = node
                l1head = l1
            else:
                l1.next = node
                l1 = node
        else:
            if not l2:
                l2 = node
                l2head = l2
            else:
                l2.next = node
                l2 = node
        i += 1
        node = n
    if l1:
        l1.next = None
    if l2:
        l2.next = None
    return Context(l1head, l2head)
