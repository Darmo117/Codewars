# noinspection PyUnresolvedReferences
Not = lambda x: x(false)(true)
# noinspection PyUnresolvedReferences
And = lambda x: lambda y: x(y)(false)
# noinspection PyUnresolvedReferences
Or = lambda x: lambda y: x(true)(y)
Xor = lambda x: lambda y: And(Or(x)(y))(Not(And(x)(y)))
