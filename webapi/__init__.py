from flask import Flask, Response, request

import webapi.unblock as lib_unblock
import webapi.unsplash as lib_unsplash

app = Flask(__name__)


@app.route('/')
def root():
    return 'Welcome to towdium.me APIs'


@app.route('/unsplash')
def unsplash():
    cat = request.args.get('category', None)
    height = request.args.get('height', '720')
    width = request.args.get('width', '1080')
    data = lib_unsplash.request(width, height, cat)
    return '' if data is None else Response(data[0], mimetype=data[1])


@app.route("/unblock/<filename>")
def unblock(filename):
    return lib_unblock.request(filename)
