#!/usr/bin/env python3
"""A basic flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    "Babel start config"
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "utc"

app.config.from_object(Config)

@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """the function that is run with a flask app"""
    return render_template('1-index.html')


# main driver function
if __name__ == '__main__':
    app.run()
