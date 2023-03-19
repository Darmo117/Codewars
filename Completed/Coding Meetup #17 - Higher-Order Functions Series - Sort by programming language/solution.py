def sort_by_language(arr):
    return sorted(arr, key=lambda user: (user['language'], user['first_name']))
