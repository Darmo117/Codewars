def get_nth(node, index: int):
    if node is None or index < 0:
        raise ValueError()
    for _ in range(index):
        node = node.next
        if node is None:
            raise ValueError()
    return node
