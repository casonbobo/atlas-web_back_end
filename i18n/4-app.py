#!/usr/bin/env python3
"""A basic flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    "Babel start config"
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """the function that is run with a flask app"""
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """match supported languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# main driver function
if __name__ == '__main__':
    app.run()
