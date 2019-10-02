"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/
"""


class Solution(object):
    def helper(self, nums, target, upper):
        left = 0
        right = len(nums)-1
        res = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res = mid
                if upper:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return res

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.helper(nums, target, False), self.helper(nums, target, True)]
