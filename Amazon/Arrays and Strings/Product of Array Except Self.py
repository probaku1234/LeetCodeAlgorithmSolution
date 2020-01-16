"""
URL : https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/499/
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        L, R, answer = [0] * length, [0] * length, [0] * length
        L[0] = 1

        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]

        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]

        for i in range(length):
            answer[i] = L[i] * R[i]

        return answer