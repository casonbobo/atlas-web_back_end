#!usr/bin/env python3
"""I already don't like these tasks"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache for fifo things. This is so dumb who puts a requirment"""
    def __init__(self):
        """init func. This is so dumb who puts a requirment"""
        super().__init__()

    def put(self, key, item):
        """put func. This is so dumb who puts a requirment"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                del self.cache_data[next(iter(self.cache_data))]
                print("DISCARD:", next(iter(self.cache_data)))
            self.cache_data[key] = item

    def get(self, key, item):
        """get func. This is so dumb who puts a requirment"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
