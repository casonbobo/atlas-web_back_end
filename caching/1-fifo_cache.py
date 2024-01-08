#!usr/bin/env python3
"""I already don't like these tasks"""
BaseCaching = __import__('base_caching').BaseCaching



class FIFOCache(BaseCaching):
    """FIFO"""
    def __init__(self):
        """init"""
        super().__init__()

    def put(self, key, item):
        """put func"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                del self.cache_data[next(iter(self.cache_data))]
                print("DISCARD:", next(iter(self.cache_data)))
            self.cache_data[key] = item

    def get(self, key, item):
        """get func"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
