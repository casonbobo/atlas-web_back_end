#!/usr/bin/env python3
"""class Auth template for the other auth systems"""
from flask import request
from typing import List, TypeVar


class Auth:
    """This is the template for the auth struct"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """This is check the auth for the path"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """This is to get the auth header"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        else:
            return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """This is to get the user"""
        return None
