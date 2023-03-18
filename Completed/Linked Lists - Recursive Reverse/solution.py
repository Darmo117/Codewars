class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse(head: Node | None) -> Node | None:
    def aux(h):
        if not h.next:
            return h, None
        tail = h.next
        h.next = None
        r, last = aux(tail)
        if last:
            last.next = h
        else:
            r.next = h
        return r, h

    return aux(head)[0] if head else None
