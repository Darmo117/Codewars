def make_readable(seconds):
    return f'{seconds // 3600:02}:{seconds // 60 % 60:02}:{seconds % 60:02}'
