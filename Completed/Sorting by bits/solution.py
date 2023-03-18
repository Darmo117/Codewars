def sort_by_bit(arr: list[int]):
    arr.sort(key=lambda n: (n.bit_count(), n))
