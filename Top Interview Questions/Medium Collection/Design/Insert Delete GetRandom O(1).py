"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/112/design/813/
"""


import random

class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict.keys():
            return False
        else:
            self.dict[val] = val
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict.keys():
            self.dict.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.dict[random.choice(self.dict.keys())]


set = RandomizedSet()
set.insert(3)
set.insert(4)
set.remove(3)
set.getRandom()