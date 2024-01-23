#!/usr/bin/env python3
"""New view for session Auth"""
from flask import Flask, request, jsonify, make_response
from api.v1.app import auth
import os

@app.route('/auth_session/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    from models import User
    user = User.search(email=email)
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = make_response(jsonify(user.to_json()))
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)

    return response
