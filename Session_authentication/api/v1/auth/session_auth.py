#!/usr/bin/env python3
"""validate if everything inherits correctly without any overloading
    validate the “switch” by using environment variables"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """This is a new structure for Auth"""
    pass
