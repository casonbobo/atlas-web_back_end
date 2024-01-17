#!/usr/bin/env python3
"""class Auth template for the other auth systems"""
from typing import List, Optional, TypeVar
from flask import request

User = TypeVar('User')


class Auth:
    """This is the template for the auth struct"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """This is check the auth for the path"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        normal_path = path if path.endswith("/") else path + "/"
        for excluded_path in excluded_paths:
            if excluded_path.endswith("/"):
                if normal_path == excluded_path:
                    return False
            else:
                if path.startwith(excluded_path):
                    return False
        return True

    def authorization_header(self, request=None) -> Optional[str]:
        """This is to get the auth header"""
        return None

    def current_user(self, request=None) -> Optional[User]:
        """This is to get the user"""
        return None
