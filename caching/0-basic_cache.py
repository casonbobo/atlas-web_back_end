#!/usr/bin/env python3
"""Merry Christmas"""


class BaseCache(BaseCaching):
    """This is a class that inheirits from caching"""
    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key, item):
        if key is None or key is not is self.cache_data:
            return None
        else:
            return self.cache_data[key]
