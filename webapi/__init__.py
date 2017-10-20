from flask import Flask, Response

import webapi.unblock as lib_unblock
import webapi.unsplash as lib_unsplash

app = Flask(__name__)


@app.route('/')
def root():
    return 'Welcome to towdium.me APIs'


@app.route('/unsplash/<path:path>')
def unsplash(path):
    data = lib_unsplash.request(path)
    return '' if data is None else Response(data[0], mimetype=data[1])


@app.route("/unblock/<filename>")
def unblock(filename):
    return lib_unblock.request(filename)
