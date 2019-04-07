import os

import requests

endpoint = 'https://tickets.mariinsky.ru/'


def is_url(obj: any) -> bool:
    return isinstance(obj, str) and (obj.startswith('/') or 'mariinsky.ru' in obj)


def normalize(url: str, host: str = None) -> str:
    if url.startswith('//'):
        url = 'https:' + url
    if url.startswith('/'):
        url = (host or endpoint) + url[1:]
    if url.endswith('/'):
        url = url + 'index.html'
    return url


def get(link: str) -> str:
    """ caching request """
    path = normalize(link).replace('https://', './').replace('http://', './')

    if not os.path.exists(path):
        directory = os.path.dirname(path)
        os.makedirs(directory, exist_ok=True)
        content = requests.get(link).content.decode('utf-8')
        with open(path, 'w') as fd:
            fd.write(content)
        return content

    with open(path) as fd:
        return fd.read()
