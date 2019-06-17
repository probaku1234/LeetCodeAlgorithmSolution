"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
"""
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]