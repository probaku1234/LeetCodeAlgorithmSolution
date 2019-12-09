"""
URL : https://leetcode.com/explore/interview/card/google/65/design-4/3090/
"""
from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

cache = LRUCache(2)
cache.put(2, 1)
cache.put(2,2)
cache.get(2)
cache.put(1,1)
cache.put(4,1)
cache.get(2)
