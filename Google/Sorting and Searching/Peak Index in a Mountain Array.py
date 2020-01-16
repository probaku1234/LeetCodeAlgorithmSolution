"""
URL : https://leetcode.com/explore/interview/card/google/63/sorting-and-searching-4/3084/
"""

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for index in range(len(A)-1):
            if A[index] > A[index+1]:
                return index

    def v2(self, A):
        left, right = 0, len(A) - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] < A[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left