def is_ruby_coming(lst):
    return any(entry['language'] == 'Ruby' for entry in lst)
