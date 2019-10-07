"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/804/
"""


class Solution(object):
    def binary_search(self, nums, left, right, target):
        if left > right:
            return -1

        mid = (left+right)//2

        if target == nums[mid]:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                return self.binary_search(nums, left, mid-1, target)
            else:
                return self.binary_search(nums, mid+1, right, target)
        else:
            if nums[mid] < target <= nums[right]:
                return self.binary_search(nums, mid+1, right, target)
            else:
                return self.binary_search(nums, left, mid-1, target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums, 0, len(nums)-1, target)