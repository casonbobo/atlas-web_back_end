#!/usr/bin/env python3
"""Merry Christmas"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """This is a class that inheirits from caching"""
    def put(self, key, item):
        """put func. This is so dumb who puts a requirment"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get func. This is so dumb who puts a requirment"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
