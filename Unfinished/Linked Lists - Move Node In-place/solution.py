def move_node(source, dest):
    if not source or not dest or not source.data:
        raise ValueError()
    data = source.data
    node = source
    prev = None
    while node.next:
        if prev:
            prev.data = node.data
        prev = node
        node = node.next
    if prev:
        prev.next = None
    # noinspection PyUnresolvedReferences
    n = Node(dest.data)
    n.next = dest.next
    dest.next = n
    dest.data = data
