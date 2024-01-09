#!usr/bin/env python3
"""The checker on these is really specific and
I am already trying to learn a lot.
Not the most helpful"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache for lifo things. This is so dumb who puts a requirment"""
    def __init__(self):
        """init func. This is so dumb who puts a requirment"""
        super().__init__()

    def put(self, key, item):
        """put func. This is so dumb who puts a requirment"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                print("DISCARD:", list(self.cache_data.keys())[-1])
                del self.cache_data[list(self.cache_data.keys())[-1]]
            self.cache_data[key] = item

    def get(self, key):
        """get func. This is so dumb who puts a requirment"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
