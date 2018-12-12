#!/usr/bin/env python3
from flask import Flask, request
import os
import urllib.request

app = Flask(__name__)

@app.route('/env/<env>')
def show_env(env):
    return os.environ.get(env)

@app.route('/fetch')
def fetch_env():
    url = request.args.get('url', '')
    with urllib.request.urlopen(url) as response:
        return response.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
