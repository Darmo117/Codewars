class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def sorted_merge(first: Node | None, second: Node | None) -> Node:
    if not first:
        return second
    elif not second:
        return first
    out = head = None
    while first or second:
        if first and (not second or first.data < second.data):
            if not head:
                out = head = first
            else:
                out.next = first
                out = first
            first = first.next
        else:
            if not head:
                out = head = second
            else:
                out.next = second
                out = second
            second = second.next
    return head
