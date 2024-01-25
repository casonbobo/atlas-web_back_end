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

@users_bp.route("/", methods=["POST"])
def users():
    email = request.form.get("email")
    password = request.form.get("password")
    
    if not email or not password:
        raise BadRequest("Missing email or password")
    try:
        user = auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
