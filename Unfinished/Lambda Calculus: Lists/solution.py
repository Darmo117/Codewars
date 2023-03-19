# noinspection PyUnresolvedReferences
APPEND = lambda l: lambda e: PAIR(IS_EMPTY)()
# noinspection PyUnresolvedReferences
PREPEND = lambda l: lambda e: PAIR(IS_EMPTY)(PAIR(e)(l))
