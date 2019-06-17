"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
"""
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums[len(nums) - 1 - i])

        for i in range(k):
            nums.pop()

