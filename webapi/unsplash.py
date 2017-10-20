from mimetypes import guess_extension, guess_type
from multiprocessing import Lock
from os import makedirs, listdir, remove
from os.path import join, splitext, exists
from threading import Thread
from time import time, sleep

from requests import get
from requests.exceptions import ReadTimeout

from webapi.constants import cache as cache_root

try:
    FileNotFoundError
except NameError:
    # noinspection PyShadowingBuiltins
    FileNotFoundError = IOError

cache = join(cache_root, 'unsplash')
none_category = '_none'
lock = Lock()
count = 0
workers = set()


def request(path):
    ret = find_cache(path)
    if ret:
        fetch_cache(path)
        return ret
    else:
        return fetch_online(path)


def find_cache(path):
    global count
    path = join(cache, path)
    try:
        with lock:
            files = listdir(path)
            if len(files) == 0:
                return None
            else:
                dest = join(path, files[count % len(files)])
                count = count + 1
                mime = guess_type(dest)[0]
                with open(dest, 'rb') as f:
                    return f.read(), mime
    except (FileNotFoundError, OSError):
        return None


def fetch_online(path):
    url = 'https://source.unsplash.com/' + path
    # a typical link: https://source.unsplash.com/category/nature/2600x500
    try:
        resp = get(url, timeout=10, stream=True)
        ret = resp.raw.read()
        mime = resp.headers['Content-Type']
        write_cache(ret, mime, path)
        return ret, mime
    except ReadTimeout:
        fetch_cache(path)
        return None


def write_cache(content, mime, path):
    if len(content) < 100:
        return
    file_path = join(cache, path)
    with lock:
        if not exists(file_path):
            makedirs(file_path)
        files = sorted(listdir(file_path), key=lambda name: int(splitext(name)[0]))
        dest = join(file_path, str(int(time())) + guess_extension(mime))
        with open(dest, 'wb') as f:
            f.write(content)
        if len(files) > 2:
            remove(join(file_path, files[0]))


def fetch_cache(path):
    def fetch():
        if path not in workers:
            try:
                workers.add(path)
                url = 'https://source.unsplash.com/' + path
                resp = get(url, timeout=20, stream=True)
                ret = resp.raw.read()
                mime = resp.headers['Content-Type']
                write_cache(ret, mime, path)
                sleep(2)
                workers.remove(path)
            except ReadTimeout:
                pass

    thread = Thread(target=fetch)
    # thread.setDaemon(True)
    thread.start()
