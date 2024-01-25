#!/usr/bin/env python3
"""Starts and runs a basuc flask app"""
from flask import Flask, jsonify, request, abort, redirect
import uuid
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    """basic Flask app"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """register a user"""
    try:
        email = request.form.get("email")
        password = request.form.get("password")
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@app.route("/sessions", methods=["POST"])
def login():
    """login method"""
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        abort(401)

    try:
        if AUTH.valid_login(email, password):
            session_id = str(uuid.uuid4())
            response = jsonify({"email": email})
            response.set_cookie("session_id", session_id)
            return response
        else:
            abort(401)
    except ValueError:
        abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """logout method"""
    session_id = request.cookies.get('session_id', None)
    user = AUTH.get_user_from_session_id(session_id)

    if session_id is None or user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route("/profile", methods=["GET"])
def profile():
    """profile structure"""
    session_id = request.cookies.get('session_id', None)
    user = AUTH.get_user_from_session_id(session_id)

    if session_id is None or user is None:
        abort(403)

    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """generate a token"""
    try:
        email = request.form.get('email')
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
