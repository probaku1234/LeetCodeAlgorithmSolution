"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/801/
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index in range(len(nums)):
            if (index - 1 < 0 or nums[index-1] < nums[index]) and (index + 1 >= len(nums) or nums[index+1] < nums[index]):
                return index