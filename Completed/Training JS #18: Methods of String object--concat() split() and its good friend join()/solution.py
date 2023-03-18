def split_and_merge(string: str, separator: str) -> str:
    return ' '.join(separator.join(word) for word in string.split())
