import re


class ReNameAbleClass:
    @classmethod
    def change_class_name(cls, new_name):
        if not re.fullmatch(r'[A-Z]\w*', new_name):
            raise ValueError(new_name)
        cls.__name__ = new_name

    @classmethod
    def __str__(cls):
        return f'Class name is: {cls.__name__}'
