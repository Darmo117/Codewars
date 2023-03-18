def sorted_insert(head, data):
    node = head
    prev = None
    while node and node.data < data:
        prev = node
        node = node.next
    # noinspection PyUnresolvedReferences
    n = Node(data)
    n.next = node
    if prev:
        prev.next = n
        return head
    return n
