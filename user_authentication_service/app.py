#!/usr/bin/env python3
"""Starts and runs a basuc flask app"""
from flask import Flask, jsonify, request, abort

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
def session():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        abort(400)

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
