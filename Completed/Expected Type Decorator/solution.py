class UnexpectedTypeException(TypeError):
    pass


def expected_type(return_types: tuple):
    def aux(f):
        def decorated(*args, **kwargs):
            result = f(*args, **kwargs)
            if all(not isinstance(result, t) for t in return_types):
                raise UnexpectedTypeException()
            return result

        return decorated

    return aux
