def count_if(head, func):
    count = 0
    while head:
        if func(head.data):
            count += 1
        head = head.next
    return count
