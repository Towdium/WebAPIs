from flask import Flask, Response, request

import webapi.unsplash

cache = '/var/cache/'
app = Flask(__name__)


@app.route('/')
def root():
    return 'Welcome to towdium.me APIs'


@app.route('/unsplash')
def unsplash_():
    cat = request.args.get('category', None)
    height = request.args.get('height', '720')
    width = request.args.get('width', '1080')
    data = unsplash.request(width, height, cat)
    return '' if data is None else Response(data[0], mimetype=data[1])
