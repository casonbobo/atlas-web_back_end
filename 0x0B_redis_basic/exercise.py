#!/usr/bin/env python3
"""Cache class stores an instance of the Redis client"""
import redis
import functools
from uuid import uuid4
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        method_qualname = method.__qualname__
        input_key = f"{method_qualname}:inputs"
        output_key = f"{method_qualname}:outputs"
        self. _redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


class Cache:
    """Cache class for Regis"""
    def __init__(self):
        """Init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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


def replay(cache_instance, function_qualname) -> None:
    input_key = f"{function_qualname}:inputs"
    output_key = f"{function_qualname}:outputs"
    inputs = cache_instance._redis.lrange(input_key, 0, -1)
    outputs = cache_instance._redis.lrange(output_key, 0, -1)
    history = list(zip(inputs, outputs))
    for input_data, output_data in history:
        input_str = input_data.decode('utf-8')
        output_str = input_data.decode('utf-8')
        print(f"{method.__qualname__}(*{input_str}) -> {output_str}")
