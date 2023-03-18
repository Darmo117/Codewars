def order_weight(raw_weights: str) -> str:
    weights = raw_weights.split()
    weights.sort(key=lambda w: (sum(int(c) for c in w), w))
    return ' '.join(weights)
