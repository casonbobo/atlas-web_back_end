#!/usr/bin/env python3
"""A basic flask app"""
from flask import Flask, render_template
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """match supported languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """return user dict or none"""
    user_id = request.args.get('login_as')
    if user_id:
        try:
            user_id = int(user_id)
            return users.get(user_id)
        except ValueError:
            return None
    return None


@app.before_request
def before_request():
    """sets get user equal guser"""
    g.user = get_user()


# main driver function
if __name__ == '__main__':
    app.run()
