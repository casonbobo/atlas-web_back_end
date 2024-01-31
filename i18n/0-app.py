#!/usr/bin/env python3
"""A basic flask app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """the function that is run with a flask app"""
    return 'Hello world'


# main driver function
if __name__ == '__main__':
    app.run()
