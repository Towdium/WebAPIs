from mimetypes import guess_extension, guess_type
from multiprocessing import Lock
from os import makedirs, listdir, remove
from os.path import join, splitext
from random import choice
from threading import Thread
from time import time

from requests import get
from requests.exceptions import ReadTimeout

import webapi

cache = join(webapi.cache, 'unsplash')
none_category = '_none'
lock = Lock()


def request(width, height, category=None):
    if category is not None:
        category = category.lower()
    ret = find_cache(width, height, category)
    if ret:
        fetch_cache(width, height, category)
        return ret
    else:
        return fetch_online(width, height, category)


def find_cache(width, height, category):
    if category is None:
        category = none_category
    path = join(cache, category, str(width) + '*' + str(height))
    try:
        with lock:
            files = listdir(path)
            if len(files) == 0:
                return None
            else:
                dest = join(path, choice(files))
                mime = guess_type(dest)[0]
                with open(dest, 'rb') as f:
                    return f.read(), mime
    except FileNotFoundError:
        return None


def fetch_online(width, height, category):
    url = 'https://source.unsplash.com/'
    if category is not None:
        url += 'category/' + category + '/'
    url += str(width) + 'x' + str(height) + '/'
    # a typical link: https://source.unsplash.com/category/nature/2600x500
    try:
        resp = get(url, timeout=10, stream=True)
        ret = resp.raw.read()
        mime = resp.headers['Content-Type']
        write_cache(ret, mime, width, height, category)
        return ret, mime
    except ReadTimeout:
        fetch_cache(width, height, category)
        return None


def write_cache(content, mime, width, height, category):
    if len(content) < 100:
        return

    if category is None:
        category = none_category
    path = join(cache, category, str(width) + '*' + str(height))
    with lock:
        makedirs(path, exist_ok=True)
        files = listdir(path)
        name = int(time())
        times = sorted(map(lambda i: int(splitext(i)[0]), files), reverse=True)
        if len(times) != 0 and times[0] == name:
            for i in range(1, len(times)):
                if times[i] != times[0] - i:
                    name = times[0] - i
                    break
            if times[0] == name:
                return
        dest = join(path, str(int(time())) + guess_extension(mime))
        with open(dest, 'wb') as f:
            f.write(content)
        if len(files) > 4:
            remove(join(path, [i for i in files if i.startswith(str(times[-1]))][0]))


def fetch_cache(width, height, category):
    def fetch():
        try:
            url = 'https://source.unsplash.com/'
            if category is not None:
                url += 'category/' + category + '/'
            url += str(width) + 'x' + str(height) + '/'
            resp = get(url, timeout=20, stream=True)
            ret = resp.raw.read()
            mime = resp.headers['Content-Type']
            write_cache(ret, mime, width, height, category)
        except ReadTimeout:
            pass

    thread = Thread(target=fetch)
    # thread.setDaemon(True)
    thread.start()
