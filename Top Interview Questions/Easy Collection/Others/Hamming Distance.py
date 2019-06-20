"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = x ^ y

        result = 0
        for i in range(32):
            result += (distance & 1)
            distance = distance >> 1

        return result