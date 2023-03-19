def count_developers(lst):
    return sum(user['language'] == 'JavaScript' and user['continent'] == 'Europe' for user in lst)
