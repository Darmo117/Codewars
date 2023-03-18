def sort_by_binary_ones(num_list: list[int]) -> list[int]:
    return sorted(num_list, key=lambda n: (-n.bit_count(), n.bit_length(), n))
