ENDINGS = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en'],
}


def conjugate(verb: str) -> dict[str, list[str]]:
    radical, ending = verb[:-2], verb[-2:]
    return {
        verb: [radical + end for end in ENDINGS[ending]]
    }
