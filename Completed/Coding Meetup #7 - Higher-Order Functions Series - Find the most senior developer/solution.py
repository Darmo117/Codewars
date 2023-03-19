def find_senior(lst):
    oldests = []
    for user in lst:
        if oldests and oldests[-1]['age'] < user['age']:
            oldests.clear()
        if not oldests or oldests[-1]['age'] == user['age']:
            oldests.append(user)
    return oldests
