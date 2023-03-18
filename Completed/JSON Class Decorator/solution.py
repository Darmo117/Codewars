import json


def jsonattr(filepath: str):
    with open(filepath) as f:
        attrs = json.load(f)

    def wrapper(cls):
        for k, v in attrs.items():
            setattr(cls, k, v)
        return cls

    return wrapper
