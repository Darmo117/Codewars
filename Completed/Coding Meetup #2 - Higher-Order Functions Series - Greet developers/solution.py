def greet_developers(lst):
    return [
        {
            **user,
            'greeting': f'Hi {user["firstName"]}, what do you like the most about {user["language"]}?',
        }
        for user in lst
    ]
