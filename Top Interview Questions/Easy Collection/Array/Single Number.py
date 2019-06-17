"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
"""
class Solution:
    def singleNumber(self, nums) -> int:
        res = nums[0]

        for i in range(1, len(nums)):
            res = res ^ nums[i]

        return res