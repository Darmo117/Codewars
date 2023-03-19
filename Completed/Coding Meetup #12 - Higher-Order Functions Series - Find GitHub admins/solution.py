def find_admin(lst, lang):
    return [user for user in lst if user['language'] == lang and user['githubAdmin'] == 'yes']
