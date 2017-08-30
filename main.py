from flask import Flask, Response, request
from requests import get

app = Flask(__name__)

@app.route('/')
def root():
    return 'Welcome to towdium.me APIs'

@app.route('/unsplash')
def hello_world():
    cat = request.args.get('category', None)
    height = request.args.get('height', '720')
    width = request.args.get('width', '1080')
    url = 'https://source.unsplash.com/'
    if cat is not None: url += 'category/' + cat + '/'
    url += str(width) + 'x' + height + '/'
    # a typical link: https://source.unsplash.com/category/nature/2600x500
    resp = get(url, stream=True)
    return Response(resp.raw, mimetype=resp.headers['Content-Type'])
