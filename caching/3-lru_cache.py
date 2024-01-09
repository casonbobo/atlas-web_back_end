#!usr/bin/env python3
"""I already don't like these tasks"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache for fifo things. This is so dumb who puts a requirment"""
    def __init__(self):
        """init func. This is so dumb who puts a requirment"""
        super().__init__()

    def put(self, key, item):
        """put func. This is so dumb who puts a requirment"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                print("DISCARD:", list(self.cache_data.keys())[0])
                del self.cache_data[list(self.cache_data.keys())[0]]
            self.cache_data[key] = item

    def get(self, key):
        """get func. This is so dumb who puts a requirment"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
