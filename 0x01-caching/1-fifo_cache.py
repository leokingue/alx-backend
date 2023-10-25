#!/usr/bin/env python3
"""FIFO Cache Replacement Implementation Class
"""
from baseCaching import BaseCaching


class FIFOCache(BaseCaching):
    """
    An implementation of FIFO(First In Fisrt Out) Cache
    """
    def __init__(self):
        """ Instantiation method, sets instance attributes
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = list(self.cache_data.keys())[0]
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
