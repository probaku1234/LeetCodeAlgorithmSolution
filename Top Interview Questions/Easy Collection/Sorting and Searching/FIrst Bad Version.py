"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2 # avoid overflow
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left