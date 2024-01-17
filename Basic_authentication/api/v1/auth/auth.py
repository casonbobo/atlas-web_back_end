#!/usr/bin/env python3
"""class Auth template for the other auth systems"""
from typing import List, Optional, TypeVar
from flask import request

User = TypeVar('User')

class Auth:
    """This is the template for the auth struct"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """This is check the auth for the path"""
        return False

    def authorization_header(self, request=None) -> Optional[str]:
        """This is to get the auth header"""
        return None

    def current_user(self, request=None) -> Optional[User]:
        """This is to get the user"""
        return None
