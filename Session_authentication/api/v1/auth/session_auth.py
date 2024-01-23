#!/usr/bin/env python3
"""validate if everything inherits correctly without any overloading
    validate the “switch” by using environment variables"""
from api.v1.auth.auth import Auth
import uuid


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
