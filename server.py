#!/bin/env python3
from flask import Flask
import os

app = Flask(__name__)

@app.route('/env/<env>')
def show_env(env):
    return os.environ.get(env)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
