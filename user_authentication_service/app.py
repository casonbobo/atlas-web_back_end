#!/usr/bin/env python3
"""Starts and runs a basuc flask app"""
from flask import Flas


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    """basic Flask app"""
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
