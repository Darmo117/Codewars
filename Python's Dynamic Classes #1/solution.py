import re


def class_name_changer(cls, new_name):
    if not re.fullmatch(r'[A-Z]\w*', new_name):
        raise ValueError(new_name)
    cls.__name__ = new_name
