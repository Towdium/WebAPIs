from flask import Flask, Response, request
from requests import get

app = Flask(__name__)

@app.route('/unsplash')
def hello_world():
    cat = request.args.get('category', None)
    size = request.args.get('size', None)
    url = 'https://source.unsplash.com/'
    if cat is not None: url += 'category/' + cat + '/'
    if size is not None: url += size + '/'
    resp = get(url, stream=True)
    return Response(resp.raw, mimetype=resp.headers['Content-Type'])
