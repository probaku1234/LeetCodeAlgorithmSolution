"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        else:
            return 1162261467 % n == 0