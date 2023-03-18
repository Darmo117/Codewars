def front_back_split(source, front, back):
    if not source or not source.next:
        raise ValueError()
    n1 = h1 = source
    n2 = source
    prev = None
    while n2:
        prev = n1
        n1 = n1.next
        n2 = n2.next
        if n2:
            n2 = n2.next
    prev.next = None
    front.data = h1.data
    front.next = h1.next
    back.data = n1.data
    back.next = n1.next
