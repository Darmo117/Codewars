def get_average(lst):
    return round(sum(entry['age'] for entry in lst) / len(lst))
