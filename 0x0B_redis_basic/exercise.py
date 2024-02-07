#!/usr/bin/env python3
"""Cache class stores an instance of the Redis client"""
import redis
from uuid import uuid4
from typing import Union, Callable

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

    def get(self, key: str, fn: Callable = 
            None) -> Union[str, bytes, int, float]:
        """take the str arg and callable"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> str:
        """turn into string"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """turn into int"""
        return self.get(key, int)
