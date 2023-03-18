import re

import bs4
import requests

_namespaces = '|'.join([
    'User', 'Wikipedia', 'WP', 'Project', 'WT', 'Project_talk',
    'Wikipedia_talk', 'Image', 'Image_talk', 'File', 'Mediawiki',
    'Template', 'Help', 'Category', 'Portal', 'Draft', 'TimedText',
    'Module', 'Special', 'Template_talk', 'Talk', 'File_talk',
])


def wikiscraping(url: str) -> dict[str, str]:
    response = requests.get(url)
    links = {}
    parsed = bs4.BeautifulSoup(response.text)
    anchors = parsed.body.find('div', attrs={'id': 'bodyContent'}).find_all('a')
    for anchor in anchors:
        if href := anchor.get('href'):
            # noinspection RegExpUnnecessaryNonCapturingGroup
            if m := re.fullmatch(fr'/wiki/(?!(?:{_namespaces}):)(.+)', href):
                links[m.group(1).replace('_', ' ')] = f'https://en.wikipedia.org{href}'
    return links
