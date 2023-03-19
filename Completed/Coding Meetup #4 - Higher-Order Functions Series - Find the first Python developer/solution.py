def get_first_python(users):
    for user in users:
        if user['language'] == 'Python':
            return f'{user["first_name"]}, {user["country"]}'
    return 'There will be no Python developers'
