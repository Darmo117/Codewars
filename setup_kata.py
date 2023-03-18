import pathlib
import re
import sys

import bs4
import requests

_LANG_TO_EXT = {
    'python': 'py',
    'javascript': 'js',
    'java': 'java',
}


def main():
    if len(sys.argv) != 2:
        print('Usage: setup_kata.py URL', file=sys.stderr)
        return
    url = sys.argv[1]
    m = re.fullmatch(r'(https://www.codewars.com/kata/\w+)(?:/train/(\w+))?', url)
    url, language = m.groups()
    if not language:
        print('Missing kata’s language', file=sys.stderr)
        return
    if language not in _LANG_TO_EXT:
        print(f'Unsupported kata language: {language}', file=sys.stderr)
        return
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Error {response.status_code}', file=sys.stderr)
        return
    parsed_html = bs4.BeautifulSoup(response.text, 'lxml')
    # noinspection PyUnresolvedReferences
    title = parsed_html.find('div', {'id': 'flash'}).next_sibling.find('h4').text
    title = title.replace('/', '-')
    path = pathlib.Path('Unfinished') / title
    if path.exists():
        print(f'Error: directory {path!r} already exists', file=sys.stderr)
        return
    path.mkdir()
    with (path / 'link.desktop').open('w', encoding='utf-8') as f:
        # language=Ini
        f.write(f"""\
[Desktop Entry]
Type=Link
URL={url}
""")
    (path / f'solution.{_LANG_TO_EXT[language]}').touch()
    print(f'Done, created directory "{path}"')


if __name__ == '__main__':
    main()
