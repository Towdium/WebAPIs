from os import makedirs
from os.path import join, exists

from flask import send_file, abort
from requests import get, ReadTimeout

from webapi.constants import cache as cache_root

cache = join(cache_root, 'unblock')


def request(filename):
    if filename != 'pac.pac':
        return abort(400)
    try:
        resp = get('http://pac.uku.im/pac.pac', timeout=10, stream=True)
        ret = resp.text
    except ReadTimeout:
        return abort(503)
    name = join(cache, 'pac.pac')
    if not exists(cache):
        makedirs(cache)
    with open(name, 'w') as f:
        ret = ret.replace('proxy.uku.im', 'cn.towdium.me')
        ret = ret.replace('{any:[],"bangumi.bilibili.com":[/^\/index\/ding\-count\.json$/i]}', '{any:[]}')
        f.write(ret)

    return send_file(name)
