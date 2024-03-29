#!/usr/bin/env python3
"""New view for session Auth"""
from flask import request, jsonify, make_response
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'])
def login():
    """this is a login method to handle all routes for session auth"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or email is None:
        return jsonify({"error": "email missing"}), 400
    if not password or password is None:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if not user or user is None:
        return jsonify({"error": "no user found for this email"}), 404
    user_valid = user[0]
    if not user_valid.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    import os

    session_id = auth.create_session(user_valid.id)
    response = make_response(jsonify(user_valid.to_json()))
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)

    return response
