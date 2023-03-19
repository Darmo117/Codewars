def any_match(head, pred) -> bool:
    while head:
        if pred(head.data):
            return True
        head = head.next
    return False


def all_match(head, pred) -> bool:
    while head:
        if not pred(head.data):
            return False
        head = head.next
    return True
