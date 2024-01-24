#!/usr/bin/env python3
"""Hash password for the database"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
