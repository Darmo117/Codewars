def band_name_generator(name: str) -> str:
    if name[0] == name[-1]:
        return (name[:-1] + name).title()
    return 'The ' + name.title()
