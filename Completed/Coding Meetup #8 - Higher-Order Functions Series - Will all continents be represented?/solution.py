continents = {'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'}


def all_continents(lst):
    return set(user['continent'] for user in lst) == continents
