class SpecificationMeta(type):
    def __and__(self, other):
        class And(metaclass=SpecificationMeta):
            type1 = self
            type2 = other

            def __new__(cls, row):
                return cls.type1(row) and cls.type2(row)

        return And

    def __or__(self, other):
        class Or(metaclass=SpecificationMeta):
            type1 = self
            type2 = other

            def __new__(cls, row):
                return cls.type1(row) or cls.type2(row)

        return Or

    def __invert__(self):
        class Not(metaclass=SpecificationMeta):
            type = self

            def __new__(cls, row):
                return not cls.type(row)

        return Not


class Specification(metaclass=SpecificationMeta):
    pass
