"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/
"""
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = []
        self.shuffledList = []
        for num in nums:
            self.original.append(num)
            self.shuffledList.append(num)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.shuffledList)
        return self.shuffledList