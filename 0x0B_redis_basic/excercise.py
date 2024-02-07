#!usr/bin/env python3
"""Cache class stores an instance of the Redis client"""
import redis
from uuid import uuid4
from typing import Union

class Cache:
    def __init__(self):
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid4)
        self.__redis.set(key, data)
        return key
