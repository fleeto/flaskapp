#!/usr/bin/env python3
from flask import Flask, request
import os
import urllib.request
import json

app = Flask(__name__)

@app.route('/env/<env>')
def show_env(env):
    return os.environ.get(env)

@app.route('/fetch')
def fetch_url():
    url = request.args.get('url', '')
    with urllib.request.urlopen(url) as response:
        return response.read()

@app.route('/fetch_with_header')
def fetch_with_headers():
    url = request.args.get('url', '')
    request_headers = dict(request.headers)
    with urllib.request.urlopen(url) as response:
        return  "{}\n{}".format(json.dumps(request_headers), response.read())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
