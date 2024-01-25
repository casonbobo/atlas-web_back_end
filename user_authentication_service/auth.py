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

    def create_session(self, email: str) -> str:
        """Create a session ID for a user"""
        user = self._db.find_user_by(email=email)
        if user:
            session_id = str(uuid.uuid4())
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Get a user from session"""
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy a users session"""
        if user_id is not None:
            try:
                self._db.update_user(user_id, session_id=None)
            except NoResultFound:
                return None

    def get_reset_password_token(self, email: str) -> str:
        """Generate a reset password token"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)
        return token


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a new UUID"""
    return str(uuid.uuid4())
