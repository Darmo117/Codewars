import re


def domain_name(url):
    return re.fullmatch(r'(?:https?://)?(?:[\w-]+\.)*?([\w-]+)\.(?:co\.)?\w+(?:/.*)?', url)[1]
