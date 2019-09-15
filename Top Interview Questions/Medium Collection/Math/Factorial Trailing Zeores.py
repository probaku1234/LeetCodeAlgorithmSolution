"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/816/
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            n = n//5
            res += n
        return res


