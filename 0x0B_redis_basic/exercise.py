#!/usr/bin/env python3
"""Cache class stores an instance of the Redis client"""
import redis
from uuid import uuid4
from typing import Union

class Cache:
    """Cache class for Regis"""
    def __init__(self):
        """Init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Key method"""
        key = str(uuid4)
        self._redis.set(key, data)
        return key
