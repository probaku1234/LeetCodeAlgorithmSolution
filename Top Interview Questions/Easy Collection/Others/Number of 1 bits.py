"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            result += (n & 1)
            n = n >> 1

        return result