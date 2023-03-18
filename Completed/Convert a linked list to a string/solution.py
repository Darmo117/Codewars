def stringify(node) -> str:
    out = []
    while node:
        out.append(str(node.data))
        node = node.next
    out.append('None')
    return ' -> '.join(out)
