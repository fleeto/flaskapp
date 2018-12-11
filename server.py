#!/usr/bin/env python3
from flask import Flask
import os
import urllib.request

app = Flask(__name__)

@app.route('/env/<env>')
def show_env(env):
    return os.environ.get(env)

@app.route('/fetch/<url>')
def fetch_env(url):
    with urllib.request.urlopen('http://python.org/') as response:
        return response.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
