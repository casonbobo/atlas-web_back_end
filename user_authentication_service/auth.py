#!/usr/bin/env python3
"""Hash password for the database"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user."""
        try:
            if self._db.find_user_by(email=email) is not None:
                raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            user = self._db.add_user(email=email,
                                     hashed_password=hashed_password)
            return user

    def _hash_password(self, password: str) -> bytes:
        """Hash a password"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login"""
        try:
            user = self._db.find_user_by(email=email)
            if user and bcrypt.checkpw(password.encode('utf-8'),
                                        user.hashed_password):
                return True
        except NoResultFound:
            pass
        return False


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
