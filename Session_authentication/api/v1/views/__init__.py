#!/usr/bin/env python3
""" this is the init for the views file"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *
from .session_auth import login

app_views.route('/auth_session/login', methods=['Post'](login))
User.load_from_file()
