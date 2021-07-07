#!/usr/bin/env python3
from flask import Flask, request
import os
from urllib.request import Request, urlopen
import json

app = Flask(__name__)

TRACE_HEADERS = [
    'x-request-id',
    'x-b3-traceid',
    'x-b3-spanid',
    'x-b3-parentspanid',
    'x-b3-sampled',
    'x-b3-flags',
    'x-ot-span-context'
]

@app.route('/')
def i_am_fine():
    return "I am FINE!"

@app.route('/env/<env>')
def show_env(env):
    return os.environ.get(env)

@app.route('/fetch')
def fetch_url():
    url = request.args.get('url', '')
    with urlopen(url) as response:
        return response.read()

@app.route('/fetch_with_header')
def fetch_with_headers():
    url = request.args.get('url', '')
    request_headers = dict(request.headers)
    request_headers = dict(request.headers)
    new_header = {}
    for key in request_headers.keys():
        if key.lower() in TRACE_HEADERS:
            new_header[key] = request_headers[key]

    req = Request(url, headers = new_header)
    res = urlopen(req).read()
    return  "{}\n{}".format(json.dumps(request_headers), res)

@app.route('/fetch_with_trace')
def fetch_with_trace():
    url = request.args.get('url', '')
    request_headers = dict(request.headers)
    new_header = {}
    for key in request_headers.keys():
        if key.lower() in TRACE_HEADERS:
            new_header[key] = request_headers[key]

    req = Request(url, headers = new_header)
    return urlopen(req).read()
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
