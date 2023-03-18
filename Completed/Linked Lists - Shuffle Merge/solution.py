def shuffle_merge(first, second):
    head = node = None
    i = 0
    while first or second:
        if i % 2 == 0 and first or not second:
            if not node:
                head = node = first
            else:
                node.next = first
                node = node.next
            first = first.next
        elif second:
            if not node:
                head = node = second
            else:
                node.next = second
                node = node.next
            second = second.next
        i += 1
    return head
