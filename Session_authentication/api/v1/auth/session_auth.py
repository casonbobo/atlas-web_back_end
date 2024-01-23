#!/usr/bin/env python3
"""validate if everything inherits correctly without any overloading
    validate the “switch” by using environment variables"""
from api.v1.auth.auth import Auth
from models.user import User
# from flask import Flask, request, jsonify, make_response
import uuid
import os


class SessionAuth(Auth):
    """This is a new structure for Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """creates a user_id for session"""
        if session_id is None or not isinstance(session_id, str):
            return None
        else:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns a User instance based on a cookie value"""
        if request is None:
            return None
        else:
            session_id = self.session_cookie(request)
            user_id = self.user_id_for_session_id(session_id)
            if user_id is not None:
                return User.get(user_id)
            else:
                return None

    # @app.route('/auth_session/login', methods=['POST'])
    # def login():
    #     email = request.form.get('email')
    #     password = request.form.get('password')

    #     if not email:
    #         return jsonify({"error": "email missing"}), 400
    #     if not password:
    #         return jsonify({"error": "password missing"}), 400

    #     user = User.search(email=email)
    #     if not user:
    #         return jsonify({"error": "no user found for this email"}), 404
    #     if not user.is_valid_password(password):
    #         return jsonify({"error": "wrong password"}), 401

    #     session_id = auth.create_session(user.id)
    #     response = make_response(jsonify(user.to_json()))
    #     response.set_cookie(os.getenv('SESSION_NAME'), session_id)

    #     return response
