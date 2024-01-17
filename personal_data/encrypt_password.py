#!/usr/bin/env python3
"""A function to encrypt using bcrypt"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypting passwords"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
