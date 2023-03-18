import inspect


def truth_table(boolean_function):
    argc = len(inspect.signature(boolean_function).parameters)
    names = ' '.join(chr(ord('A') + i) for i in range(argc))
    f_name = 'f' if boolean_function.__name__ == '<lambda>' else boolean_function.__name__
    res = f'{names}\t\t{f_name}({names.replace(" ", ",")})\n\n'
    for i in range(2 ** argc):
        v = list(int(b) for b in format(i, f'0{argc}b'))
        out = int(boolean_function(*v))
        res += f'{" ".join(map(str, v))}\t\t{out}\n'
    return res
